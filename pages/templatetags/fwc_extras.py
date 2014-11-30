from django import template
from pages.models import Place, Region

register = template.Library()


@register.inclusion_tag('pages/regions.html')
def get_region_list():
    return {'regions': Region.objects.all()}


@register.inclusion_tag('pages/other_places.html')
def get_other_places_list():
    return {'places': Place.objects.all()}
