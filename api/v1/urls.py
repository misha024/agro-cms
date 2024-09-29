from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import *

from .contacts.contacts_views import *
from .sliders.sliders_views import *


router = routers.DefaultRouter()

router.register(
    prefix='contacts',
    viewset=ContactsViewSet,
    basename='contacts'
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
    path('schema/', SpectacularAPIView.as_view(api_version='1.0'), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
