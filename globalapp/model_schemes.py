# ||
SETTINGS_DATA = {
    "type": "array",
    "title": "Settings Data",
    "items": {
        "type": "object",
        "properties": {
            "property_level": {
                "type": "string",
                "choices": ["LEVEL_1", "LEVEL_2", "LEVEL_3"]
            },
            "property_name": {
                "type": "string"
            },
            "property_value": {
                "type": "string"
            },
            'children': {'$ref': '#'}
        }
    }
}
