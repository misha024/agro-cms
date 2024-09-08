from .models import MainSettings, Contacts


def main_settings(request):
    try:
        settings = MainSettings.objects.get()
    except MainSettings.DoesNotExist:
        settings = None
    return {'main_settings': settings}


def main_contacts(request):
    try:
        contacts = Contacts.objects.get()
    except Contacts.DoesNotExist:
        contacts = None
    return {'main_contacts': contacts}

