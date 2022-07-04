from django.db import models
from django_jsonform.models.fields import JSONField

from teams.model_schemes import SOCIAL_MEDIA, TEAM_STAFF


# Teams
class Team(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    abbr = models.CharField(max_length=255, blank=True)
    hometown = models.CharField(max_length=255, blank=True)
    social_media = JSONField(blank=True, schema=SOCIAL_MEDIA)
    staff = JSONField(blank=True, schema=TEAM_STAFF)
    wiki = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Image pending
    # Country Pending

    class Meta:
        abstract = True
