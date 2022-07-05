from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from valor.models import (ValorAgents, ValorEventTier, ValorEventType,
                          ValorMap, ValorMatch, ValorPlayer,
                          ValorSingleMapMatch, ValorTeam, ValorTournament)


@admin.register(ValorEventTier)
class ValorEventTierAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(ValorEventType)
class ValorEventTypeAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(ValorMap)
class ValorMapAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(ValorMatch)
class ValorMatchAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(ValorPlayer)
class ValorPlayerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(ValorAgents)
class ValorAgentsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(ValorSingleMapMatch)
class ValorSingleMapMatchAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(ValorTeam)
class ValorTeamAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(ValorTournament)
class ValorTournamentAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
