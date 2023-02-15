from rest_framework import request
from rest_framework import routers
from .views import (PostNewsSet, VacancyDetail, VacancyList, ArchivedVacancyList)
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'news', PostNewsSet, basename='newspost')
router.register(r'vacancies', VacancyList, basename='vacancy')
router.register(r'archived-vacancies', ArchivedVacancyList, basename='archived-vacancy')
router.register(r'vacancies/(?P<Vacancy_id>\d+)', VacancyDetail, basename='vacancy-detail')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
