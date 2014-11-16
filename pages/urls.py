from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /pages/5/
    url(r'^(?P<region_id>\d+)/$', views.detail, name='detail'),
    # ex: /pages/5/results/
    url(r'^(?P<character_id>\d+)/results/$', views.results, name='results'),
    # # ex: /pages/5/region/
    url(r'^(?P<region_id>\d+)/region/$', views.region, name='region'),
)
