from django.contrib import admin

from globalapp.models import Country, Organizer, PlayerSetting, Region

admin.site.register(PlayerSetting)
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(Organizer)
