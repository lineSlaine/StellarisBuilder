from django.contrib import admin
from pip._vendor.rich.color import ColorType

from apps.StellarisSave.models import *

# Register your models here.

admin.site.register(StellarisSave)
admin.site.register(Planet)
admin.site.register(PlanetType)
admin.site.register(Race)
admin.site.register(RaceType)
admin.site.register(ShipType)
admin.site.register(Color)
admin.site.register(Background)
admin.site.register(Flag)
admin.site.register(FlagType)
admin.site.register(Origin)
admin.site.register(Government)
admin.site.register(Civic)
admin.site.register(Ethic)
admin.site.register(Gene)
