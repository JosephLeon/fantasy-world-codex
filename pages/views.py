from django.shortcuts import render, get_object_or_404
from pages.models import Region, Place
from pages.forms import RegionForm
from pages.forms import UserForm


def index(request):
    region_list = Region.objects.all()
    context = {'region_list': region_list}
    return render(request, 'pages/index.html', context)
    # return render(request, 'Holder')


# def detail(request, region_id):
#     region = get_object_or_404(Region, pk=region_id)
#     return render(request, 'pages/detail.html', {'region': region})


def region(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    return render(request, 'pages/region.html', {'region': region})


def place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return render(request, 'pages/place.html', {'place': place})


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
