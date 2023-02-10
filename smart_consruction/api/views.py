from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, permissions, mixins

from ..news.models import PostNews
from .serializers import (PostNewsSerializers)


class PostNewsSet(viewsets.ModelViewSet):
    queryset = PostNews.objects.all()
    serializer_class = PostNewsSerializers

    def perform_create(self, serializer):
        serializer.save()
