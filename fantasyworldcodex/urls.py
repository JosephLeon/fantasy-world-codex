from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fantasyworldcodex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^pages/', include('pages.urls', namespace='pages')),
    url(r'^admin/', include(admin.site.urls)),
)
