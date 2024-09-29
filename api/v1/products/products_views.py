from rest_framework import viewsets

from main.models import ProductsCategory
from .products_serializers import ProductsCategorySerializer


class ProductsCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsCategorySerializer
    http_method_names = ('get',)
    queryset = ProductsCategory.objects.all()
