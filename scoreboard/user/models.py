from django.db import models
from app.models import Application
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    app_username = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.CharField(max_length=100, null=True)
    id_token = models.CharField(max_length=2000, null=True)
    openid = JSONField(null=True)
    access_token = models.CharField(max_length=400, null=True)
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name='user_application',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )
    @classmethod
    def get_user(cls, username=None, openid=None, application=None):
        query = {}
        if username:
            query['app_username'] = username
        if openid:
            query['openid'] = openid
        if application:
            query['application'] = application
        print(query)
        user = User.objects.filter(**query).first()
        return user

    @classmethod
    def add_user(cls, username, full_name,
                 id_token, application, openid, avatar=None,
                 app_username=None, access_token=None):
        user = User(
            username=username,
            full_name=full_name,
            id_token=id_token,
            openid=openid,
            access_token=access_token,
            avatar=avatar,
            app_username=app_username,
            application=application
        )
        user.save()
        return user
