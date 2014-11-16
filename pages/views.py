from django.shortcuts import render
from pages.models import Region


def index(request):
    region_list = Region.objects.all()
    context = {'region_list': region_list}
    return render(request, 'pages/index.html', context)


def detail(request, character_id):
    return render(request, 'pages/index.html')


def results(request, character_id):
    return render(request, 'pages/index.html')


def region(request, region_id):
    return render(request, 'pages/index.html')
