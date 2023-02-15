from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, permissions, mixins
from rest_framework import generics
from news.models import PostNews
from vacancy.models import Vacancy
from api.serializers import (PostNewsSerializers, VacancySerializer)
from rest_framework.decorators import action


class PostNewsSet(viewsets.ModelViewSet):
    queryset = PostNews.objects.all()
    serializer_class = PostNewsSerializers

    def perform_create(self, serializer):
        serializer.save()


class VacancyList(viewsets.ModelViewSet):
    queryset = Vacancy.objects.filter(is_archived=False)
    serializer_class = VacancySerializer


class ArchivedVacancyList(viewsets.ModelViewSet):
    queryset = Vacancy.objects.filter(is_archived=True)
    serializer_class = VacancySerializer


class VacancyDetail(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    def put(self, request, *args, **kwargs):
        vacancy = self.get_object()
        vacancy.title = request.data['title']
        vacancy.description = request.data['description']
        vacancy.date_expired = request.data['date_expired']
        vacancy.save()
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        vacancy = self.get_object()
        if 'is_archived' in request.data:
            if request.data['is_archived']:
                vacancy.archive()
        return self.partial_update(request, *args, **kwargs)
