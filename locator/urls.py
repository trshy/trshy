from django.conf.urls import url

from .views import (
    index_view,
    profile_view,
)

urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^profile/$', profile_view, name='profile'),

]
