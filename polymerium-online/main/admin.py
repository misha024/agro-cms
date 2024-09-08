from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


@admin.register(MainSettings)
class MainSettingsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        try:
            settings = MainSettings.objects.get()
            return HttpResponseRedirect(reverse('admin:main_mainsettings_change', args=[settings.pk]))
        except MainSettings.DoesNotExist:
            return HttpResponseRedirect(reverse('admin:main_mainsettings_add'))

    def has_add_permission(self, request):
        return not MainSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        try:
            settings = Contacts.objects.get()
            return HttpResponseRedirect(reverse('admin:main_contacts_change', args=[settings.pk]))
        except Contacts.DoesNotExist:
            return HttpResponseRedirect(reverse('admin:main_contacts_add'))

    def has_add_permission(self, request):
        return not Contacts.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ProductsCategory)
admin.site.register(Products)
admin.site.register(SliderCards)
admin.site.register(SliderCardsDescriptions)
