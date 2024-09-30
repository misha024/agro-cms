from rest_framework import viewsets

from .contacts_serializers import *


class ContactsViewSet(viewsets.ModelViewSet):
    serializer_class = ContactsSerializer
    http_method_names = ('get', 'patch',)
    queryset = Contacts.objects.all()
