from rest_framework import serializers

from main.models import *


class SliderDescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderCardsDescriptions
        fields = ['description']


class SlidersSerializer(serializers.ModelSerializer):
    descriptions = SliderDescriptionsSerializer(many=True)

    class Meta:
        model = SliderCards
        fields = ['title', 'descriptions', 'logo', 'href']
