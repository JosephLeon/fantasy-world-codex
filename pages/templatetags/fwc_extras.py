from django.shortcuts import get_object_or_404
from django import template
from pages.models import Place, Region

register = template.Library()


@register.inclusion_tag('pages/regions.html')
def get_region_list():
    return {'regions': Region.objects.all()}


@register.inclusion_tag('pages/other_places.html')
def get_other_places_list(place_id):
    context_dict = {}

    places = Place.objects.all()
    context_dict['places'] = places
    this_object = get_object_or_404(Place, pk=place_id)
    context_dict['this_object'] = this_object
    return context_dict
