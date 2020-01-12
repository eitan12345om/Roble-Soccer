import logging

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from rest_framework import generics

from games.forms import GameForm, PlayerForm
from games.models import Game, Player
from games.serializers import GameSerializer

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


def index(request):
    games = Game.objects.order_by('datetime')

    context = {
        'games': games
    }

    return render(request, 'games/index.html', context)


class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    all_players = Player.objects.filter(game_id=game_id).order_by('id')
    playing = all_players[:game.max_players]
    waitlist = all_players[game.max_players:]

    new_player_form = PlayerForm()

    context = {
        'game': game,
        'playing': playing,
        'waitlist': waitlist,
        'new_player_form': new_player_form,
    }

    return render(request, "games/detail.html", context)


def new_player(request, game_id):
    if request.method == 'POST':
        form = PlayerForm(request.POST)

        if form.is_valid():
            player = form.save(commit=False)
            player.game_id = game_id

            logger.info(f"Creating new player -- game_id: {player.game_id} -- name: {player.name}")

            player.save()
            return redirect(reverse('games:detail', args=(player.game_id,)))

    return redirect(reverse('games:index'))


def delete_player(request, player_id):
    if request.method == 'POST':
        player = Player.objects.get(id=player_id)
        logger.info(
            f"Deleting player -- game_id: {player.game_id} -- name: {player.name}")

        game_id = player.game_id
        player.delete()

        return redirect(reverse('games:detail', args=(game_id,)))

    return redirect(reverse('games:index'))


def new_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)

        if form.is_valid():
            game = form.save()
            logger.info(
                f"Created new game -- location: {game.location} -- datetime: {game.datetime} -- max_players: {game.max_players}")

            return redirect(reverse('games:detail', args=(game.id,)))
    else:
        form = GameForm()

    context = {
        'form': form
    }

    return render(request, "games/new_game.html", context)
