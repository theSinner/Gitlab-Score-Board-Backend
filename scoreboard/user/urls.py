from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        'auth$',
        views.UserAuth.as_view(),
        name='user_auth'
    ),
    url(
        'auth/done',
        views.UserAuthDone.as_view(),
        name='user_auth_done'
    ),
]
