from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /pages/regions/5/
    # url(r'^regions/(?P<region_id>\d+)/$', views.detail, name='detail'),
    url(r'^regions/(?P<region_id>\d+)/$', views.region, name='region'),
    # /pages/places/5/
    url(r'^places/(?P<place_id>\d+)/$', views.place, name='place'),
)
