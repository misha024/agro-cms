import requests
from django.shortcuts import render
from .models import *


def index(request):
    sliders_data = SliderCards.objects.all()
    categories = ProductsCategory.objects.all()
    return render(request, 'index.html', {
        'sliders_data': sliders_data,
        'categories': categories,
    })


def contact_submit(request):
    if request.method == 'POST' and request.POST.get('phone'):

        main_settings = MainSettings.objects.get() if MainSettings.objects.count() else None
        if (
            main_settings is None
            or not main_settings.site_domain
            or not main_settings.telegram_token
            or not main_settings.telegram_group
        ):
            return render(request, 'error.html')

        domain_name = main_settings.site_domain
        telegram_token = main_settings.telegram_token
        telegram_group = main_settings.telegram_group

        phone_number = request.POST.get('phone')
        message = f"""<b>Получена новая заявка!</b>
<b>Веб-сайт:</b> <code>{domain_name}</code>
<b>Телефон:</b><code>{phone_number}</code>"""
        requests.get(f"https://api.telegram.org" 
                     f"/bot{telegram_token}"
                     f"/sendMessage"
                     f"?chat_id={telegram_group}"
                     f"&text={message}"
                     f"&parse_mode=html")

        return render(request, 'save.html')

    return render(request, 'index.html')