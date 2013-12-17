from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^page/(?P<post>\d+)$', 'blog.views.page'),
    url(r'^posts/$', 'blog.views.posts_range'),
)