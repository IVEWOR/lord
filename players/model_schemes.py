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
