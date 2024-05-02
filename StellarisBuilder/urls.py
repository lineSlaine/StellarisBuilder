"""
URL configuration for StellarisBuilder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from django.conf import settings

from apps.StellarisSave.views import *

router = routers.DefaultRouter()
router.register(r'api/stellaris/ethics', EthicView)
router.register(r'api/stellaris/planet', PlanetView)
router.register(r'api/stellaris/planet/type', PlanetTypeView)
router.register(r'api/stellaris/background', BackgroundView)
router.register(r'api/stellaris/flag', FlagView)
router.register(r'api/stellaris/flag/type', FlagTypeView)
router.register(r'api/stellaris/race', RaceView)
router.register(r'api/stellaris/race/type', RaceTypeView)
router.register(r'api/stellaris/ship', ShipTypeView)
router.register(r'api/stellaris/origin', OriginView)
router.register(r'api/stellaris/government', GovernmentView)
router.register(r'api/stellaris/civic', CivicView)
router.register(r'api/stellaris/gene', GeneView)
router.register(r'api/stellaris/color', ColorView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

# if settings.DEBUG:
#  import debug_toolbar
#   urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
