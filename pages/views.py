from django.shortcuts import render, get_object_or_404
from pages.models import Region, Place, Building, Character, Item
from pages.forms import RegionForm, PlaceForm, CharacterForm

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers


def index(request):
    context = {}
    region_list = Region.objects.all()
    context['region_list'] = region_list
    place_list = Place.objects.all()
    context['place_list'] = place_list
    building_list = Building.objects.all()
    context['building_list'] = building_list
    character_list = Character.objects.all()
    context['character_list'] = character_list
    return render(request, 'pages/index.html', context)


def region(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    return render(request, 'pages/region.html', {'region': region})


def place(request, place_id):
    context_dict = {}

    # Place.
    place = get_object_or_404(Place, pk=place_id)
    context_dict['place'] = place

    # Buildings and characters owned by this place.
    buildings = Building.objects.filter(place=place_id)
    context_dict['buildings'] = buildings
    characters = Character.objects.filter(place=place_id)
    context_dict['characters'] = characters

    return render(request, 'pages/place.html', context_dict)


def building(request, building_id):
    context = {}

    # Building.
    building = get_object_or_404(Building, pk=building_id)
    context['building'] = building

    # Characters that belong to this building.
    characters = Character.objects.filter(building=building_id)
    context['characters'] = characters

    return render(request, 'pages/building.html', context)


def character(request, character_id):
    context_dict = {}

    # Character.
    character = get_object_or_404(Character, pk=character_id)
    context_dict['character'] = character

    # Items that belong to this character.
    items = Item.objects.filter(character=character_id)
    context_dict['items'] = items

    return render(request, 'pages/character.html', context_dict)


def item(request, item_id):
    context_dict = {}

    # Item.
    item = get_object_or_404(Item, pk=item_id)
    context_dict['item'] = item

    return render(request, 'pages/item.html', context_dict)


def add_region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = RegionForm()

    return render(request, 'pages/add_region.html', {'form': form})


def add_place(request):

    places = Place.objects.all()
    id_list = {}
    for place in places:
        id_list['biggest_id'] = place.id
    pid = id_list['biggest_id'] + 1

    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('pages:place', args=(pid,)))
        else:
            print form.errors
    else:
        form = PlaceForm()

    return render(request, 'pages/add_place.html', {'form': form})


def add_character(request):

    characters = Character.objects.all()
    id_list = {}
    for character in characters:
        id_list['biggest_id'] = character.id
    cid = id_list['biggest_id'] + 1

    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('pages:character', args=(cid,)))
        else:
            print form.errors
    else:
        form = CharacterForm()

    return render(request, 'pages/add_character.html', {'form': form})


def feeds_subcat(request, region_id):
    json_subcat = serializers.serialize("json", Place.objects.filter(region=region_id))
    return HttpResponse(json_subcat, mimetype="application/javascript")


# hdef feeds_subcat(request, cat_id):
#     from django.core import serializers
#     json_subcat = serializers.serialize("json", ProductSubCategory.objects.filter(prodcat = cat_id))
#     return HttpResponse(json_subcat, mimetype="application/javascript")
