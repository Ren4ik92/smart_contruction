from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('codyp/', views.codyp, name='codyp'),
    path('tp/', views.tp, name='tp'),
    path('cod78/', views.cod87, name='cod78'),
    path('mangerok/', views.mangerok, name='mangerok'),
    path('d2/', views.d2, name='d2'),

]
