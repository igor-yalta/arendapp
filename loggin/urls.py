from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', 'loggin.views.login'),
    url(r'^logout/$', 'loggin.views.logout'),
    url(r'^register/$', 'loggin.views.register'),
)