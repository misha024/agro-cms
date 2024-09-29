from rest_framework import serializers

from main.models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['phone', 'email', 'telegram']
