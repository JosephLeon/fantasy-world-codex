from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_region/$', views.add_region, name='add_region'),
    url(r'^add_place/$', views.add_place, name='add_place'),
    url(r'^regions/(?P<region_id>\d+)/$', views.region, name='region'),
    url(r'^places/(?P<place_id>\d+)/$', views.place, name='place'),
    url(r'^buildings/(?P<building_id>\d+)/$', views.building, name='building'),
)
