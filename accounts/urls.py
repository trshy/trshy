from django.conf.urls import url

from .views import (
    login_view,
    logout_view,
    register_view,
    change_password_view,
)

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register_view, name='register'),
    url(r'^change_profile/$', change_password_view, name='change_profile'),
]
