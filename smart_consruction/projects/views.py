from django.shortcuts import render


def projects(request):
    template = 'projects/projects.html'
    return render(request, template)


def codyp(request):
    template = 'projects/codyp.html'
    return render(request, template)


def tp(request):
    template = 'projects/tp.html'
    return render(request, template)


def cod87(request):
    template = 'projects/cod78.html'
    return render(request, template)


def mangerok(request):
    template = 'projects/mangerok.html'
    return render(request, template)

def d2(request):
    template = 'projects/d2.html'
    return render(request, template)
