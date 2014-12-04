from django.shortcuts import render, get_object_or_404
from pages.models import Region, Place, Building, Character, Item
from pages.forms import RegionForm, PlaceForm, CharacterForm
# from pages.forms import UserForm

import json
from clever_selects.views import ChainedSelectChoicesView
from django.views.generic.detail import BaseDetailView
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import EMPTY_VALUES
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.utils.cache import add_never_cache_headers


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
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = PlaceForm()

    return render(request, 'pages/add_place.html', {'form': form})


def add_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CharacterForm()

    return render(request, 'pages/add_character.html', {'form': form})


# class AjaxChainedPlace(ChainedSelectChoicesView):

#     def get_choices(self):
#         regions = {
#             'Xanadu': [
#                 'City of Krakzin', 'Sweet Water', 'blaa', 'lskdjflskdf'
#             ],
#             'Northern Mountains': [
#                 'crap', 'sdlfkjsld', '984759384'
#             ],
#             'Karjik': [
#                 'Hi', 'Bye'
#             ],
#             'Elthadrun': [
#                 'Elves'
#             ],
#         }
#         choices = []
#         try:
#             continent_countries = regions[self.parent_value]
#             for country in continent_countries:
#                 choices.append((country, country))
#         except KeyError:
#             return []
#         return choices
        # COUNTRIES = {
            # CONTINENT_NORTH_AMERICA: [
            #     COUNTRY_ALASKA, COUNTRY_CANADA, COUNTRY_USA, COUNTRY_MEXICO
            # ],
        # }
        # regions = {
        #     Xanadu: [
        #         COUNTRY_ALASKA, COUNTRY_CANADA, COUNTRY_USA, COUNTRY_MEXICO
        #     ],
        # }
        # choices = []
        # try:
        #     continent_countries = regions[self.parent_value]
        #     for country in continent_countries:
        #         choices.append((country, country))
        # except KeyError:
        #     return []
        # return choices
# class AjaxChainedView(BaseDetailView):
#     """
#     View to handle the ajax request for the field options.
#     """

#     def get(self, request, *args, **kwargs):
#         field = request.GET.get('field')
#         parent_value = request.GET.get("parent_value")

#         vals_list = []
#         for x in range(1, 6):
#             vals_list.append(x*int(parent_value))

#         choices = tuple(zip(vals_list, vals_list))

#         response = HttpResponse(
#             json.dumps(choices, cls=DjangoJSONEncoder),
#             mimetype='application/javascript'
#         )
#         add_never_cache_headers(response)
#         return response
