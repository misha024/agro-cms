from rest_framework import viewsets, permissions, generics, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from main.models import Contacts
from .contacts_serializers import *


class ContactsViewSet(viewsets.ViewSet):
    def list(self, request):
        contact = Contacts.objects.first()
        if contact:
            serializer = ContactsSerializer(contact)
            return Response(serializer.data)
        return Response({"detail": "Контакты не найдены"}, status=404)
