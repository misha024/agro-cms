from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import *

from .contacts.contacts_views import ContactsViewSet
from .sliders.sliders_views import SlidersViewSet
from .products.products_views import ProductsCategoryViewSet

from .custom.contact_submit import ContactSubmit

router = routers.DefaultRouter()

router.register(
    prefix='contacts',
    viewset=ContactsViewSet,
    basename='contacts'
)

router.register(
    prefix='categories',
    viewset=ProductsCategoryViewSet,
    basename='categories'
)

router.register(
    prefix='sliders',
    viewset=SlidersViewSet,
    basename='sliders'
)

urlpatterns = [
    path('', include(router.urls)),

    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.authtoken')),
]

urlpatterns += [
    path('contact-submit/', ContactSubmit.as_view(), name='contact-submit')
]

urlpatterns += [
    path('schema/', SpectacularAPIView.as_view(api_version='1.0'), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
