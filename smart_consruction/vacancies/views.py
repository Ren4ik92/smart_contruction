from django.shortcuts import render


def vacancies(request):
    template = 'vacancies/vacancies.html'
    return render(request, template)


def zip_vacancies(request):
    template = 'vacancies/archive.html'
    return render(request, template)
