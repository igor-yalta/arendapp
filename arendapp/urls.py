from django.conf.urls import patterns, include, url
import article
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'arendapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('article.urls')),
    url(r'^auth/', include('loggin.urls')),
)
if settings.DEBUG:
        urlpatterns += patterns('',
                                #REMOVE IT in production phase
                                (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT})
                              )