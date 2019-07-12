from django.db import models
from model_utils import Choices
# Create your models here.

TYPES = Choices(
    ('gitlab', 'Gitlab'),
)


class Application(models.Model):
    name = models.CharField(max_length=100, unique=True)
    application_id = models.CharField(max_length=400)
    secret_token = models.CharField(max_length=400)
    url = models.CharField(max_length=100, null=True, blank=True)
    app_type = models.CharField(max_length=10, null=True, choices=TYPES)
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    @classmethod
    def find_application(cls, application_id):
        return Application.objects.filter(
            application_id=application_id
        ).first()
