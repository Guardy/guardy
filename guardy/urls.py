from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

import lib.audit
lib.audit

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.page'),
        url(r'^page/(?P<page_no>\d+)$', 'home.views.page'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)), )