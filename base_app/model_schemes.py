# ||
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

# ||
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

# ||
TEAM_HISTORY = {
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

# ||
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


# ||
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

# ||
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

# ||
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

# ||
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

# ||
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

# ||
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

# ||
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

# ||
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
