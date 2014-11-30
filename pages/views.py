from django.shortcuts import render, get_object_or_404
from pages.models import Region, Place, Building, Character
from pages.forms import RegionForm, PlaceForm
from pages.forms import UserForm


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

    return render(request, 'pages/building.html', context)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # profile.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render(
        request,
        'pages/registration.html',
        {'user_form': user_form, 'registered': registered}
    )


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
