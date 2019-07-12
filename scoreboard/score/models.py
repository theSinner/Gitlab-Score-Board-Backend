from django.db import models
from app.models import Application
# Create your models here.

SCORE_TYPE = (
    ('task', 'Task'),
)

ACTION_TYPE = (
    ('done', 'Done'),
    ('rejected', 'Rejected'),
    ('blocked', 'Blocked')
)


class ScoreItem(models.Model):
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name="score_item_application"
    )
    team = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choice=SCORE_TYPE)
    tag = models.CharField(max_length=100, null=True, blank=True)
    score = models.IntegerField(default=0)
    if_not_assignee_extra = models.IntegerField(default=0)
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )
