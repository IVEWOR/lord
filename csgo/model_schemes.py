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
