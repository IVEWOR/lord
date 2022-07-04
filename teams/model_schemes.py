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
