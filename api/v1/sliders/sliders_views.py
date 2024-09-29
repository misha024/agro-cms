from rest_framework import viewsets, mixins

from main.models import SliderCards
from .sliders_serializers import SlidersSerializer


class SlidersViewSet(viewsets.ModelViewSet):
    serializer_class = SlidersSerializer
    http_method_names = ('get',)
    queryset = SliderCards.objects.all()
