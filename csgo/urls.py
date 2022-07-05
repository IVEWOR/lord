from django.urls import path

from csgo import views

urlpatterns = [
    path("players/<slug:slug>/", views.player_detail, name="player_detail"),
]
