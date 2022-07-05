from django.shortcuts import render

from csgo.models import CsPlayer


def player_detail(request, slug):
    cs_player = CsPlayer.objects.get(slug=slug)
    return render(request, "csgo/cs_player_detail.html", {
        "cs_player": cs_player,
    })
