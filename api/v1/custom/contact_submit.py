import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from main.models import MainSettings


TELEGRAM_MESSAGE = lambda domain_name, phone_number: (
    f"<b>Получена новая заявка!</b>\n"
    f"<b>Веб-сайт:</b> <code>{domain_name}</code>\n"
    f"<b>Телефон:</b> <code>{phone_number}</code>"
)


class ContactSubmit(APIView):
    def post(self, request):
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        if not ip_address:
            return Response({'error': 'Не удалось определить IP-адрес.'}, status=status.HTTP_400_BAD_REQUEST)

        if cache.get(f'contact_submit_{ip_address}'):
            return Response({'error': 'Вы уже отправляли заявку. Повторите позже.'}, status=status.HTTP_429_TOO_MANY_REQUESTS)

        phone_number = request.POST.get('phone')
        if not phone_number:
            return Response({'error': 'Укажите правильный телефон.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            settings = MainSettings.objects.get()
        except MainSettings.DoesNotExist:
            return Response({'error': 'Неизвестная ошибка. [ER1]'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        settings_safe = settings.site_domain and settings.telegram_token and settings.telegram_group
        if not settings_safe:
            return Response({'error': 'Неизвестная ошибка. [ER2]'}, status=status.HTTP_400_BAD_REQUEST)

        domain_name = settings.site_domain
        telegram_token = settings.telegram_token
        telegram_group = settings.telegram_group

        telegram_send = requests.get(
            f"https://api.telegram.org/bot{telegram_token}/sendMessage?"
            f"chat_id={telegram_group}&text={TELEGRAM_MESSAGE(domain_name, phone_number)}&parse_mode=html"
        )

        if telegram_send.status_code != 200:
            return Response({'error': 'Неизвестная ошибка. [ER3]'}, status=status.HTTP_400_BAD_REQUEST)

        cache.set(f'contact_submit_{ip_address}', True, timeout=12 * 3600)

        return Response({"message": "Заявка успешно создана"}, status=status.HTTP_201_CREATED)


#
# ERROR LIST:
#   [ER1] - Настройки не найдены.
#   [ER2] - Некорректные настройки сайта.
#   [ER3] - Ошибка отправки сообщения в Telegram.
#