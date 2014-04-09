from django.conf.urls import patterns, include, url
from .views import WelcomeView, AboutUsView

# Uncomment the next two lines to enable the admin:


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc.views.home', name='home'),
    # url(r'^gisc/', include('gisc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^welcome$', WelcomeView.as_view(), name = 'welcome'),
    url(r'^aboutus$', AboutUsView.as_view(), name = 'aboutus'),
)
