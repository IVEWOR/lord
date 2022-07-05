from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from csgo.models import (CsEventTier, CsEventType, CsMap, CsMatch, CsPlayer,
                         CsRole, CsSingleMapMatch, CsTeam, CsTournament)


@admin.register(CsEventTier)
class CsEventTierAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(CsEventType)
class CsEventTypeAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(CsMap)
class CsMapAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(CsMatch)
class CsMatchAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(CsPlayer)
class CsPlayerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(CsRole)
class CsRoleAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(CsSingleMapMatch)
class CsSingleMapMatchAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(CsTeam)
class CsTeamAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(CsTournament)
class CsTournamentAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
