from django.db import models
from django_jsonform.models.fields import JSONField

SOCIAL_MEDIA = {
    "type": "array",
    "title": "Social Media",
    "items": {
        'type': 'object',
        'properties': {
            "website": {
                "type": "string",
                "choices": ["Twitter", "Facebook", "Instagram",
                            "YouTube", "Twitch", "Steam", "Discord", "Faceit"]
            },
            "url": {
                "type": "string"
            }
        }
    }
}


# Players
class Player(models.Model):

    STATUS_CHOICES = (
        ("A", "Active"),
        ("I", "Inactive"),
        ("R", "Retired"),
        ("U", "Unknown"),
    )

    YEARS_ACTIVE = {
        "type": "object",
        "keys": {
            "start_year": {
                "type": "string"
            },
            "end_year": {
                "type": "string"
            }
        },
    }
    Team_History = {
        "type": "array",
        "title": "Team History",
        "items": {
            "type": "object",
            "properties": {
                "team": {
                    "type": "string"
                },
                "start_date": {
                    "type": "string",
                    "format": "datetime"
                },
                "end_date": {
                    "type": "string",
                    "format": "datetime"
                },
                "team_url": {
                    "type": "string"
                }
            }
        }
    }
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    native_name = models.CharField(max_length=255, blank=True)
    born = models.DateField(blank=True, null=True)
    hometown = models.CharField(max_length=255, blank=True)
    # birth country -- pending
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default="A")
    years_active = JSONField(schema=YEARS_ACTIVE, blank=True)
    team = models.ForeignKey(
        "Team", on_delete=models.SET_NULL, blank=True, null=True)
    role = models.ForeignKey(
        "Role", on_delete=models.SET_NULL, blank=True, null=True)
    earnings = models.PositiveIntegerField(blank=True, null=True)
    nicknames = models.CharField(max_length=255, blank=True)
    # profile_image -- pending
    social_media = JSONField(blank=True, schema=SOCIAL_MEDIA)
    team_history = JSONField(blank=True, schema=Team_History)
    team_mates = models.ManyToManyField("self", blank=True)
    wiki = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "csgo_players"
        ordering = ["updated_at"]
        verbose_name = "Player"
        verbose_name_plural = "Players"


# Teams
class Team(models.Model):
    TEAM_STAFF = {
        "type": "array",
        "title": "Team Staff",
        "items": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "choices": ["Coach", "Manager", "CEO", "Founder"]
                },
                "name": {
                    "type": "string"
                }
            }
        }
    }
    title = models.CharField(max_length=255, blank=True)
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

    def __str__(self):
        return self.title

    class Meta:
        db_table = "csgo_teams"
        ordering = ["updated_at"]
        verbose_name = "Team"
        verbose_name_plural = "Teams"


# Roles
class Role(models.Model):
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    wiki = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "csgo_roles"
        ordering = ["updated_at"]
        verbose_name = "Role"
        verbose_name_plural = "Roles"


# Maps
class Map(models.Model):
    title = models.CharField(max_length=255, blank=True)
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
        ordering = ["updated_at"]
        verbose_name = "Map"
        verbose_name_plural = "Maps"


PLAYERS_STATS_TOUR = {
    "type": "array",
    "title": "Players Stats",
    "items": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string"
            },
            "team": {
                "type": "string"
            },
            "kills": {
                "type": "number"
            },
            "deaths": {
                "type": "number"
            },
            "assists": {
                "type": "number"
            },
            "kd": {
                "type": "number"
            },
            "kast": {
                "type": "number"
            },
            "adr": {
                "type": "number"
            },
            "total_matches": {
                "type": "number"
            },
            "wins": {
                "type": "number"
            },
            "losses": {
                "type": "number"
            },
            "total_rounds": {
                "type": "number"
            },
            "round_wins": {
                "type": "number"
            },
            "round_losses": {
                "type": "number"
            },
        }
    }
}

TEAM_STATS = {
    "type": "array",
    "title": "Team Stats",
    "items": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string"
            },
            "total_matches_played": {
                "type": "number"
            },
            "total_matches_won": {
                "type": "number"
            },
            "total_matches_lost": {
                "type": "number"
            },
            "total_rounds_played": {
                "type": "number"
            },
            "total_rounds_won": {
                "type": "number"
            },
            "total_rounds_lost": {
                "type": "number"
            },
            "best_player": {
                "type": "string"
            },
            "worst_player": {
                "type": "string"
            }
        }
    }
}

PRIZE_DISTRIBUTION = {
    "type": "array",
    "title": "Prize Distribution",
    "items": {
        "type": "object",
        "properties": {
            "rank": {
                "type": "number"
            },
            "prize": {
                "type": "string"
            },
            "prize_percentage": {
                "type": "number"
            },
            "name": {
                "type": "string"
            }
        }
    }
}


# Tournaments
class Tournament(models.Model):
    BROADCASTERS = {
        "type": "array",
        "title": "Broadcasters",
        "items": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "url": {
                    "type": "string"
                }
                # logo pending
            }
        }
    }
    TALENT = {
        "type": "array",
        "title": "Talent",
        "items": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                # image pending
            }
        }
    }

    MATCH_SCHEDULE = {
        "type": "array",
        "title": "Match Schedule",
        "items": {
            "type": "object",
            "properties": {
                "stage": {
                    "type": "string"
                },
                "type": "array",
                "title": "Match Type",
                "items": {
                    "type": "object",
                    "properties": {
                        "match_number": {
                            "type": "integer"
                        },
                        "date": {
                            "type": "string",
                            "format": "datetime"
                        },
                        "team_1": {
                            "type": "string"
                        },
                        "team_2": {
                            "type": "string"
                        },
                        "team_1_url": {
                            "type": "string"
                        },
                        "team_2_url": {
                            "type": "string"
                        }
                    }
                }
            }
        }
    }
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    abbr = models.CharField(max_length=255, blank=True)
    # image -- pending
    # cover -- pending
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True)
    # country -- pending
    venue = models.CharField(max_length=255, blank=True)
    # organizer -- pending
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
    participant_teams = models.ManyToManyField("Team", blank=True)
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
        ordering = ["updated_at"]
        verbose_name = "Tournament"
        verbose_name_plural = "Tournaments"


MAP_POOL = {
    "type": "array",
    "title": "Map Pool",
    "items": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string"
            },
            "url": {
                "type": "string"
            },
            "selected_by": {
                "type": "string"
            }
        }
    }
}


PLAYERS_STATS = {
    "type": "array",
    "title": "Players Stats",
    "items": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string"
            },
            "team": {
                "type": "string"
            },
            "kills": {
                "type": "number"
            },
            "deaths": {
                "type": "number"
            },
            "assists": {
                "type": "number"
            },
            "kd": {
                "type": "number"
            },
            "kast": {
                "type": "number"
            },
            "adr": {
                "type": "number"
            },
        }
    }
}


# Matches
class Match(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(
        "Tournament", on_delete=models.SET_NULL, null=True,  blank=True)
    team_1 = models.ForeignKey(
        "Team", on_delete=models.SET_NULL, null=True,
        related_name="match_team_1", blank=True)
    team_2 = models.ForeignKey(
        "Team", on_delete=models.SET_NULL, null=True,
        related_name="match_team_2", blank=True)
    team_1_score = models.PositiveIntegerField(default=0)
    team_2_score = models.PositiveIntegerField(default=0)
    start_date_time = models.DateTimeField(blank=True, null=True)
    is_match_finished = models.BooleanField(default=False)
    mvp = models.ForeignKey(
        "Player", on_delete=models.SET_NULL, null=True, blank=True)
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
        ordering = ["updated_at"]
        verbose_name = "Match"
        verbose_name_plural = "Matches"


# SingleMapMatch
class SingleMapMatch(models.Model):
    id = models.AutoField(primary_key=True)
    match = models.ForeignKey(
        "Match", on_delete=models.SET_NULL, null=True, blank=True)
    team_1 = models.ForeignKey(
        "Team", on_delete=models.SET_NULL, null=True,
        related_name="single_match_team_1")
    team_2 = models.ForeignKey(
        "Team", on_delete=models.SET_NULL, null=True,
        related_name="single_match_team_2")
    team_1_score = models.PositiveIntegerField(default=0)
    team_2_score = models.PositiveIntegerField(default=0)
    map = models.ForeignKey(
        "Map", on_delete=models.SET_NULL, null=True, blank=True)
    map_number = models.PositiveIntegerField(default=1)
    start_date_time = models.DateTimeField(blank=True, null=True)
    is_match_finished = models.BooleanField(default=False)
    mvp = models.ForeignKey(
        "Player", on_delete=models.SET_NULL, null=True, blank=True)
    team_1_players = models.ManyToManyField(
        "Player", related_name="team_1_players", blank=True)
    team_2_players = models.ManyToManyField(
        "Player", related_name="team_2_players", blank=True)
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
        ordering = ["updated_at"]
        verbose_name = "Single Map Match"
        verbose_name_plural = "Single Map Matches"


# EventTypes
class EventType(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "csgo_event_types"
        ordering = ["updated_at"]
        verbose_name = "Event Type"
        verbose_name_plural = "Event Types"


# EventTiers
class EventTier(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "csgo_event_tiers"
        ordering = ["updated_at"]
        verbose_name = "Event Tier"
        verbose_name_plural = "Event Tiers"
