from django.urls import path
from . import views

app_name = 'vacancies'

urlpatterns = [
    path('', views.vacancies, name='vacancies'),
    path('archive/', views.zip_vacancies, name='zip_vacancies'),
]
