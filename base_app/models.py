from commerce.models import PcSpec
from django.db import models
from django.utils.text import slugify
from django_jsonform.models.fields import JSONField
from globalapp.models import Country

from base_app.model_schemes import (SOCIAL_MEDIA, TEAM_HISTORY, TEAM_STAFF,
                                    YEARS_ACTIVE)


# Players
class Player(models.Model):
    STATUS_CHOICES = (
        ("A", "Active"),
        ("I", "Inactive"),
        ("R", "Retired"),
        ("U", "Unknown"),
        ("M", "Migrated"),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    native_name = models.CharField(max_length=255, blank=True)
    alternate_ids = models.CharField(max_length=255, blank=True)
    born = models.DateField(blank=True, null=True)
    hometown = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True,
        related_name="%(app_label)s_%(class)s_related")
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default="A")
    # migrated new profile
    years_active = JSONField(schema=YEARS_ACTIVE, blank=True)
    earnings = models.PositiveIntegerField(blank=True, null=True)
    nicknames = models.CharField(max_length=255, blank=True)
    # profile_image -- pending
    social_media = JSONField(blank=True, schema=SOCIAL_MEDIA)
    team_history = JSONField(blank=True, schema=TEAM_HISTORY)
    team_mates = models.ManyToManyField(
        "self", blank=True)
    setup = models.ForeignKey(
        PcSpec, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_related")
    wiki = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# Teams
class Team(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    abbr = models.CharField(max_length=255, blank=True)
    hometown = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True,
        related_name="%(app_label)s_%(class)s_related")
    social_media = JSONField(blank=True, schema=SOCIAL_MEDIA)
    staff = JSONField(blank=True, schema=TEAM_STAFF)
    wiki = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Image pending

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
