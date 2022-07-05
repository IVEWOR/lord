from base_app.models import (BaseSimpleOption, Match, Player, SingleMapMatch,
                             Team, Tournament)
from django.db import models
from django.urls import reverse


# Players
class CsPlayer(Player):
    team = models.ForeignKey(
        "CsTeam", on_delete=models.SET_NULL, blank=True, null=True)
    role = models.ForeignKey(
        "CsRole", on_delete=models.SET_NULL, blank=True, null=True)

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

    def get_absolute_url(self):
        return reverse("csgo:team_detail", kwargs={"slug": self.slug})


# Roles
class CsRole(BaseSimpleOption):
    class Meta:
        db_table = "csgo_roles"
        ordering = ["-updated_at"]
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("csgo:role_detail", kwargs={"slug": self.slug})


# Maps
class CsMap(BaseSimpleOption):
    class Meta:
        db_table = "csgo_maps"
        ordering = ["-updated_at"]
        verbose_name = "Map"
        verbose_name_plural = "Maps"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("csgo:map_detail", kwargs={"slug": self.slug})


# Tournaments
class CsTournament(Tournament):
    event_type = models.ForeignKey(
        "CsEventType", on_delete=models.SET_NULL, null=True,  blank=True)
    event_tier = models.ForeignKey(
        "CsEventTier", on_delete=models.SET_NULL, null=True,  blank=True)
    maps = models.ManyToManyField("CsMap", blank=True)
    participant_teams = models.ManyToManyField("CsTeam", blank=True)

    class Meta:
        db_table = "csgo_tournaments"
        ordering = ["-updated_at"]
        verbose_name = "Tournament"
        verbose_name_plural = "Tournaments"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("csgo:tournament_detail", kwargs={"slug": self.slug})


# Match
class CsMatch(Match):
    event = models.ForeignKey(
        "CsTournament", on_delete=models.SET_NULL, null=True,  blank=True)
    team_1 = models.ForeignKey(
        "CsTeam", on_delete=models.SET_NULL, null=True,
        related_name="match_team_1", blank=True)
    team_2 = models.ForeignKey(
        "CsTeam", on_delete=models.SET_NULL, null=True,
        related_name="match_team_2", blank=True)
    team_1_players = models.ManyToManyField(
        "CsPlayer", related_name="team_1_players", blank=True)
    team_2_players = models.ManyToManyField(
        "CsPlayer", related_name="team_2_players", blank=True)
    mvp = models.ForeignKey(
        "CsPlayer", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "csgo_match"
        ordering = ["-updated_at"]
        verbose_name = "Match"
        verbose_name_plural = "Matches"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("csgo:match_detail", kwargs={"slug": self.slug})


# Single Map Match
class CsSingleMapMatch(SingleMapMatch):
    match = models.ForeignKey(
        "CsMatch", on_delete=models.SET_NULL, null=True, blank=True)
    map = models.ForeignKey(
        "CsMap", on_delete=models.SET_NULL, null=True, blank=True)
    mvp = models.ForeignKey(
        "CsPlayer", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "csgo_single_map_match"
        ordering = ["-updated_at"]
        verbose_name = "Single Map Match"
        verbose_name_plural = "Single Map Matches"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("csgo:single_map_match_detail", kwargs={"slug": self.slug})


# Event Tier
class CsEventTier(BaseSimpleOption):
    class Meta:
        db_table = "csgo_event_tiers"
        ordering = ["-updated_at"]
        verbose_name = "Event Tier"
        verbose_name_plural = "Event Tiers"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("csgo:event_tier_detail", kwargs={"slug": self.slug})


# Event Types
class CsEventType(BaseSimpleOption):
    class Meta:
        db_table = "csgo_event_types"
        ordering = ["-updated_at"]
        verbose_name = "Event Type"
        verbose_name_plural = "Event Types"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("csgo:event_type_detail", kwargs={"slug": self.slug})
