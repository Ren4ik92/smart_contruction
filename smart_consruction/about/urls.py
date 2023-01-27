from django.urls import path
from django.views.generic.base import TemplateView

app_name = 'about'

urlpatterns = [
    path('', TemplateView.as_view(template_name='about/about_company.html'), name='about_company'),
    path('contacts/', TemplateView.as_view(template_name='about/contacts.html'), name='contacts')
]