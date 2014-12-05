from __future__ import unicode_literals

from selectable.base import ModelLookup
from selectable.registry import registry

from pages.models import Place, Building


class PlaceLookup(ModelLookup):
    model = Place
    search_fields = ('name__icontains', )

    def get_query(self, request, term):
        results = super(PlaceLookup, self).get_query(request, term)
        print results
        region = request.GET.get('region', '')
        print region
        if region:
            results = results.filter(region=region)
        return results

    def get_item_label(self, item):
        return "%s, %s" % (item.name, item.region)


registry.register(PlaceLookup)


class BuildingLookup(ModelLookup):
    model = Building
    search_fields = ('name__icontains', )

    def get_query(self, request, term):
        results = super(BuildingLookup, self).get_query(request, term)
        print results
        place = request.GET.get('place', '')
        print place
        if place:
            results = results.filter(place=place)
        return results

    # def create_item(self, item):
        # return "%s, %s" % (item.name, item.place)

    # def get_item_label(self, item):
    #     return "%s, %s" % (item.name, item.place)


registry.register(BuildingLookup)
