from django import template
from models.pages import Place, Region

register = template.Library()


@register.inclusion_tag('pages/regions.html')
def get_region_list():
    return {'regions': Region.objects.all()}


@register.inclusion_tag('pages/places.html')
def get_place_list():
    return {'places': Place.objects.all()}
