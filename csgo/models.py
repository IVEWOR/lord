from base_app.models import Player, Team
from django.db import models
from django.urls import reverse
from django_jsonform.models.fields import JSONField
from globalapp.models import Country, Organizer

from csgo.model_schemes import (BROADCASTERS, MAP_POOL, MATCH_SCHEDULE,
                                PLAYERS_STATS, PLAYERS_STATS_TOUR,
                                PRIZE_DISTRIBUTION, SOCIAL_MEDIA, TALENT,
                                TEAM_STATS)


# Players
class CsPlayer(Player):
    team = models.ForeignKey(
        "CsTeam", on_delete=models.SET_NULL, blank=True, null=True)
    role = models.ForeignKey(
        "Role", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = "csgo_players"
        ordering = ["-updated_at"]
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("csgo:player_detail", kwargs={"slug": self.slug})


# Teams
class CsTeam(Team):

    class Meta:
        db_table = "csgo_teams"
        ordering = ["-updated_at"]
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.title


# Roles
class Role(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    wiki = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "csgo_roles"
        ordering = ["-updated_at"]
        verbose_name = "Role"
        verbose_name_plural = "Roles"


# Maps
class Map(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    abbr = models.CharField(max_length=255, blank=True)
    wiki = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "csgo_maps"
        ordering = ["-updated_at"]
        verbose_name = "Map"
        verbose_name_plural = "Maps"


# Tournaments
class Tournament(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    abbr = models.CharField(max_length=255, blank=True)
    # image -- pending
    # cover -- pending
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True)
    venue = models.CharField(max_length=255, blank=True)
    organizer = models.ForeignKey(
        Organizer, on_delete=models.SET_NULL, blank=True, null=True)
    event_type = models.ForeignKey(
        "EventType", on_delete=models.SET_NULL, null=True,  blank=True)
    event_tier = models.ForeignKey(
        "EventTier", on_delete=models.SET_NULL, null=True,  blank=True)
    social_media = JSONField(blank=True, schema=SOCIAL_MEDIA)
    maps = models.ManyToManyField("Map", blank=True)
    event_format = models.TextField(blank=True)
    total_matches = models.PositiveIntegerField(default=16)
    match_schedule = JSONField(blank=True, schema=MATCH_SCHEDULE)
    total_teams = models.PositiveIntegerField(default=22)
    participant_teams = models.ManyToManyField("CsTeam", blank=True)
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

    def __str__(self):
        return self.title

    class Meta:
        db_table = "csgo_tournaments"
        ordering = ["-updated_at"]
        verbose_name = "Tournament"
        verbose_name_plural = "Tournaments"


# Matches
class Match(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    event = models.ForeignKey(
        "Tournament", on_delete=models.SET_NULL, null=True,  blank=True)
    team_1 = models.ForeignKey(
        "CsTeam", on_delete=models.SET_NULL, null=True,
        related_name="match_team_1", blank=True)
    team_2 = models.ForeignKey(
        "CsTeam", on_delete=models.SET_NULL, null=True,
        related_name="match_team_2", blank=True)
    team_1_score = models.PositiveIntegerField(default=0)
    team_2_score = models.PositiveIntegerField(default=0)
    start_date_time = models.DateTimeField(blank=True, null=True)
    is_match_finished = models.BooleanField(default=False)
    mvp = models.ForeignKey(
        "CsPlayer", on_delete=models.SET_NULL, null=True, blank=True)
    map_pool = JSONField(blank=True, schema=MAP_POOL)
    overall_players_stats = JSONField(
        blank=True, schema=PLAYERS_STATS, null=True)
    aftermath = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        title = "{} vs {} at {}".format(
            self.team_1.title, self.team_2.title, self.event.title
        )
        return title

    class Meta:
        db_table = "csgo_matches"
        ordering = ["-updated_at"]
        verbose_name = "Match"
        verbose_name_plural = "Matches"


# SingleMapMatch
class SingleMapMatch(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    match = models.ForeignKey(
        "Match", on_delete=models.SET_NULL, null=True, blank=True)
    team_1 = models.ForeignKey(
        "CsTeam", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="single_match_team_1")
    team_2 = models.ForeignKey(
        "CsTeam", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="single_match_team_2")
    team_1_score = models.PositiveIntegerField(default=0)
    team_2_score = models.PositiveIntegerField(default=0)
    map = models.ForeignKey(
        "Map", on_delete=models.SET_NULL, null=True, blank=True)
    map_number = models.PositiveIntegerField(default=1)
    start_date_time = models.DateTimeField(blank=True, null=True)
    is_match_finished = models.BooleanField(default=False)
    mvp = models.ForeignKey(
        "CsPlayer", on_delete=models.SET_NULL, null=True, blank=True)
    team_1_players = models.ManyToManyField(
        "CsPlayer", related_name="team_1_players", blank=True)
    team_2_players = models.ManyToManyField(
        "CsPlayer", related_name="team_2_players", blank=True)
    players_stats = JSONField(blank=True, schema=PLAYERS_STATS)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        title = "{} vs {} - {}".format(
            self.team_1.title, self.team_2.title, self.map_number
        )
        return title

    class Meta:
        db_table = "csgo_single_map_matches"
        ordering = ["-updated_at"]
        verbose_name = "Single Map Match"
        verbose_name_plural = "Single Map Matches"


# EventTypes
class EventType(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True,)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "csgo_event_types"
        ordering = ["-updated_at"]
        verbose_name = "Event Type"
        verbose_name_plural = "Event Types"


# EventTiers
class EventTier(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True,)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "csgo_event_tiers"
        ordering = ["-updated_at"]
        verbose_name = "Event Tier"
        verbose_name_plural = "Event Tiers"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("csgo:event_tier_detail", kwargs={"slug": self.slug})
