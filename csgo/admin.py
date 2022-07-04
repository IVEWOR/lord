from django.contrib import admin

from csgo.models import (EventTier, EventType, Map, Match, Player, Role,
                         SingleMapMatch, Team, Tournament)

admin.site.register(Player)
admin.site.register(Role)
admin.site.register(Team)
admin.site.register(Map)
admin.site.register(EventType)
admin.site.register(EventTier)
admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(SingleMapMatch)
