from django.shortcuts import render, get_object_or_404
from pages.models import Region, Place


def index(request):
    region_list = Region.objects.all()
    context = {'region_list': region_list}
    return render(request, 'pages/index.html', context)


def detail(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    return render(request, 'pages/detail.html', {'region': region})


def place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return render(request, 'pages/place.html', {'place': place})


def results(request, character_id):
    return render(request, 'pages/index.html')


def region(request, region_id):
    return render(request, 'pages/index.html')
