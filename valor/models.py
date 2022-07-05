from base_app.models import (BaseSimpleOption, Match, Player, SingleMapMatch,
                             Team, Tournament)
from django.db import models
from django.urls import reverse


# Players
class ValorPlayer(Player):
    team = models.ForeignKey(
        "ValorTeam", on_delete=models.SET_NULL, blank=True, null=True)
    role = models.ForeignKey(
        "ValorAgents", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = "valor_players"
        ordering = ["-updated_at"]
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("valor:player_detail", kwargs={"slug": self.slug})


# Teams
class ValorTeam(Team):
    class Meta:
        db_table = "valor_teams"
        ordering = ["-updated_at"]
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("valor:team_detail", kwargs={"slug": self.slug})


# Roles
class ValorAgents(BaseSimpleOption):
    class Meta:
        db_table = "valor_agents"
        ordering = ["-updated_at"]
        verbose_name = "Agent"
        verbose_name_plural = "Agents"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("valor:agent_detail", kwargs={"slug": self.slug})


# Maps
class ValorMap(BaseSimpleOption):
    class Meta:
        db_table = "valor_maps"
        ordering = ["-updated_at"]
        verbose_name = "Map"
        verbose_name_plural = "Maps"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("valor:map_detail", kwargs={"slug": self.slug})


# Tournaments
class ValorTournament(Tournament):
    event_type = models.ForeignKey(
        "ValorEventType", on_delete=models.SET_NULL, null=True,  blank=True)
    event_tier = models.ForeignKey(
        "ValorEventTier", on_delete=models.SET_NULL, null=True,  blank=True)
    maps = models.ManyToManyField("ValorMap", blank=True)
    participant_teams = models.ManyToManyField("ValorTeam", blank=True)

    class Meta:
        db_table = "valor_tournaments"
        ordering = ["-updated_at"]
        verbose_name = "Tournament"
        verbose_name_plural = "Tournaments"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("valor:tournament_detail", kwargs={"slug": self.slug})


# Match
class ValorMatch(Match):
    event = models.ForeignKey(
        "ValorTournament", on_delete=models.SET_NULL, null=True,  blank=True)
    team_1 = models.ForeignKey(
        "ValorTeam", on_delete=models.SET_NULL, null=True,
        related_name="match_team_1", blank=True)
    team_2 = models.ForeignKey(
        "ValorTeam", on_delete=models.SET_NULL, null=True,
        related_name="match_team_2", blank=True)
    team_1_players = models.ManyToManyField(
        "ValorPlayer", related_name="team_1_players", blank=True)
    team_2_players = models.ManyToManyField(
        "ValorPlayer", related_name="team_2_players", blank=True)
    mvp = models.ForeignKey(
        "ValorPlayer", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "valor_match"
        ordering = ["-updated_at"]
        verbose_name = "Match"
        verbose_name_plural = "Matches"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("valor:match_detail", kwargs={"slug": self.slug})


# Single Map Match
class ValorSingleMapMatch(SingleMapMatch):
    match = models.ForeignKey(
        "ValorMatch", on_delete=models.SET_NULL, null=True, blank=True)
    map = models.ForeignKey(
        "ValorMap", on_delete=models.SET_NULL, null=True, blank=True)
    mvp = models.ForeignKey(
        "ValorPlayer", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "valor_single_map_match"
        ordering = ["-updated_at"]
        verbose_name = "Single Map Match"
        verbose_name_plural = "Single Map Matches"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("valo:single_map_match_detail", kwargs={"slug": self.slug})


# Event Tier
class ValorEventTier(BaseSimpleOption):
    class Meta:
        db_table = "valor_event_tiers"
        ordering = ["-updated_at"]
        verbose_name = "Event Tier"
        verbose_name_plural = "Event Tiers"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("valor:event_tier_detail", kwargs={"slug": self.slug})


# Event Types
class ValorEventType(BaseSimpleOption):
    class Meta:
        db_table = "valor_event_types"
        ordering = ["-updated_at"]
        verbose_name = "Event Type"
        verbose_name_plural = "Event Types"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("valor:event_type_detail", kwargs={"slug": self.slug})
