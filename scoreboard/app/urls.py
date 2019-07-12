from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        'auth',
        views.AppAuth.as_view(),
        name='app_auth'
    ),
]
