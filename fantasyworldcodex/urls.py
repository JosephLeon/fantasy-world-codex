from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/pages/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fantasyworldcodex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('pages.urls', namespace='pages')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
