import os
import requests
from django.shortcuts import render
from .models import ProductsCategory, Contacts, SliderCards
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GROUP_CHAT_ID = os.getenv("GROUP_CHAT_ID")


def index(request):
    sliders_data = SliderCards.objects.all()
    categories = ProductsCategory.objects.all()
    return render(request, 'index.html', {
        'sliders_data': sliders_data,
        'categories': categories,
    })


# POST REQUEST {'phone': '+1 111 111 11 11'}
def contact_submit(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        if phone_number:
            message = f"""
<b>Получена новая заявка!</b>
<b>Телефон:</b><code>{phone_number}</code>
            """
            requests.get(f"https://api.telegram.org" 
                         f"/bot{TOKEN}"
                         f"/sendMessage"
                         f"?chat_id={GROUP_CHAT_ID}"
                         f"&text={message}"
                         f"&parse_mode=html")

        return render(request, 'save.html')

    return render(request, 'index.html')