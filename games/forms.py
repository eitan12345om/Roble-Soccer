from django import forms

from .models import Game, Player


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('location', 'datetime', 'max_players', 'min_players')


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('name',)
