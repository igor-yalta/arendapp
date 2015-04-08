from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

import article

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'arendapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/articles/all/$', 'article.views.articles'),
    url(r'^', 'article.views.articles'),

)
