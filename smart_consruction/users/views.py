from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreationFrom


class SignUp(CreateView):
    form_class = CreationFrom
    success_url = reverse_lazy('index')

