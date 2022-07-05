from django.shortcuts import render

from csgo.models import CsPlayer


def player_detail(request, slug):
    player = CsPlayer.objects.get(slug=slug)
    return render(request, "player-detail.html", {
        "player": player,
    })
