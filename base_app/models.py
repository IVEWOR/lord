from commerce.models import PcSpec
from django.db import models
from django.utils.text import slugify
from django_jsonform.models.fields import JSONField
from filer.fields.image import FilerImageField
from globalapp.models import Country, Organizer, PlayerSetting

from base_app.model_schemes import (BROADCASTERS, MAP_POOL, MATCH_SCHEDULE,
                                    PLAYERS_STATS, PLAYERS_STATS_TOUR,
                                    PRIZE_DISTRIBUTION, SOCIAL_MEDIA, TALENT,
                                    TEAM_HISTORY, TEAM_STAFF, TEAM_STATS,
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
    avatar = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    native_name = models.CharField(max_length=255, blank=True)
    alternate_ids = models.CharField(max_length=255, blank=True)
    born = models.DateField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
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
    social_media = JSONField(blank=True, schema=SOCIAL_MEDIA)
    team_history = JSONField(blank=True, schema=TEAM_HISTORY)
    team_mates = models.ManyToManyField(
        "self", blank=True)
    setup = models.ForeignKey(
        PcSpec, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_related")
    settings = models.ForeignKey(
        PlayerSetting, on_delete=models.SET_NULL,
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
    logo = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    hometown = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True)
    social_media = JSONField(blank=True, schema=SOCIAL_MEDIA)
    staff = JSONField(blank=True, schema=TEAM_STAFF)
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


# Tournaments
class Tournament(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    abbr = models.CharField(max_length=255, blank=True)
    avatar = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    cover_image = FilerImageField(
        null=True, blank=True, on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_related")
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True)
    venue = models.CharField(max_length=255, blank=True)
    organizer = models.ForeignKey(
        Organizer, on_delete=models.SET_NULL, blank=True, null=True)
    social_media = JSONField(blank=True, schema=SOCIAL_MEDIA)
    event_format = models.TextField(blank=True)
    total_matches = models.PositiveIntegerField(default=16)
    match_schedule = JSONField(blank=True, schema=MATCH_SCHEDULE)
    total_teams = models.PositiveIntegerField(default=22)
    prize_pool = models.CharField(max_length=20, blank=True)
    prize_distribution = JSONField(blank=True, schema=PRIZE_DISTRIBUTION)
    teams_stats = JSONField(blank=True, schema=TEAM_STATS)
    players_stats = JSONField(blank=True, schema=PLAYERS_STATS_TOUR)
    broadcasters = JSONField(blank=True, schema=BROADCASTERS)
    talent = JSONField(blank=True, schema=TALENT)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# Matches
class Match(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    avatar = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    team_1_score = models.PositiveIntegerField(default=0)
    team_2_score = models.PositiveIntegerField(default=0)
    start_date_time = models.DateTimeField(blank=True, null=True)
    is_match_finished = models.BooleanField(default=False)
    map_pool = JSONField(blank=True, schema=MAP_POOL)
    overall_players_stats = JSONField(
        blank=True, schema=PLAYERS_STATS, null=True)
    aftermath = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# SingleMapMatch
class SingleMapMatch(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    team_1_score = models.PositiveIntegerField(default=0)
    team_2_score = models.PositiveIntegerField(default=0)
    map_number = models.PositiveIntegerField(default=1)
    start_date_time = models.DateTimeField(blank=True, null=True)
    is_match_finished = models.BooleanField(default=False)
    players_stats = JSONField(blank=True, schema=PLAYERS_STATS)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# BaseSimpleOptions
class BaseSimpleOption(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    avatar = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
