from django.urls import path
from apps.user.views import indexPageView

app_name = 'user'

urlpatterns = [
    path('', indexPageView, name='index'),
]