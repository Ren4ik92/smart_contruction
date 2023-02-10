from rest_framework import request
from rest_framework import routers
from .views import (PostNewsSet)
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'news', PostNewsSet, basename='newspost')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
