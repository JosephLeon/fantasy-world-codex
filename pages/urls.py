from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^regions/(?P<region_id>\d+)/$', views.region, name='region'),
    url(r'^places/(?P<place_id>\d+)/$', views.place, name='place'),
    url(r'^register/$', views.register, name='register'),
)
