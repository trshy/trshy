from django.conf.urls import url

from .views import (
    index_view,
    profile_view,
    map_view,
    rate_view,
    add_view
)

urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^map/$', map_view, name='map'),
    url(r'^map/add', add_view, name='add'),
    url(r'^rate', rate_view, name='rate'),

]
