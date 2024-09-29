from rest_framework import serializers

from main.models import Products, ProductsCategory


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'logo']


class ProductsCategorySerializer(serializers.ModelSerializer):
    products = ProductsSerializer(source='product', many=True, read_only=True)

    class Meta:
        model = ProductsCategory
        fields = ['name', 'products']
