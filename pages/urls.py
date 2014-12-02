from django.conf.urls import patterns, url

from pages import views
from views import AjaxChainedView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_region/$', views.add_region, name='add_region'),
    url(r'^add_place/$', views.add_place, name='add_place'),
    url(r'^add_character/$', views.add_character, name='add_character'),
    url(r'^ajax/custom-chained-view-url/$', AjaxChainedView.as_view(), name='ajax_chained_view'),
    url(r'^regions/(?P<region_id>\d+)/$', views.region, name='region'),
    url(r'^places/(?P<place_id>\d+)/$', views.place, name='place'),
    url(r'^buildings/(?P<building_id>\d+)/$', views.building, name='building'),
    url(r'^characters/(?P<character_id>\d+)/$', views.character, name='character'),
    url(r'^items/(?P<item_id>\d+)/$', views.item, name='item'),
)
