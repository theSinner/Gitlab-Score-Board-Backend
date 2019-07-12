from django.db import models
from app.models import Application
from django.contrib.postgres.fields import ArrayField
# Create your models here.

SCORE_RULE_SUBJECT = (
    ('task', 'Task'),
)

SCORE_RULE_TYPE = (
    ('positive', 'Positive'),
    ('negative', 'Negative')
)


class ScoreRule(models.Model):
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name="score_item_application"
    )
    subject = models.CharField(max_length=20, choices=SCORE_RULE_SUBJECT)
    type = models.CharField(max_length=20, choices=SCORE_RULE_TYPE)
    tag = models.CharField(max_length=100, null=True, blank=True)
    score = models.IntegerField(default=0)
    exlcude_usernames = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
    )
    include_usernames = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
    )
    exlcude_teams = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
    )
    include_teams = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
    )
    if_not_assignee_extra = models.IntegerField(default=0)
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )
