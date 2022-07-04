from django.contrib import admin

from csgo.models import (CsPlayer, CsTeam, EventTier, EventType, Map, Match,
                         Role, SingleMapMatch, Tournament)

admin.site.register(CsPlayer)
admin.site.register(Role)
admin.site.register(CsTeam)
admin.site.register(Map)
admin.site.register(EventType)
admin.site.register(EventTier)
admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(SingleMapMatch)
