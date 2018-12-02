from django.conf.urls import url

from .views import (
    index_view,
    profile_view,
)

urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^map/$', profile_view, name='map'),
    url(r'^trashcan(?P<id>[\d-]+)/$', profile_view, name='trashcan'),

]
