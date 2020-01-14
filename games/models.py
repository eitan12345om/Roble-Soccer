from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import localtime, now


class Game(models.Model):
    DEFAULT_MAX_NUM_PLAYERS = 18
    DEFAULT_MIN_NUM_PLAYERS = 14

    location = models.CharField(max_length=100, default='Roble Field')
    datetime = models.DateTimeField('when')
    max_players = models.PositiveSmallIntegerField(default=DEFAULT_MAX_NUM_PLAYERS)
    min_players = models.PositiveSmallIntegerField(default=DEFAULT_MIN_NUM_PLAYERS)

    def __str__(self):
        return f'Game at {self.location} on {self.datetime}'

    def is_in_future(self):
        return self.datetime > localtime(now())

    def clean(self):
        super().clean()

        if self.datetime:
            present = localtime(now())
            if self.datetime < present:
                raise ValidationError('A new game must be set in the future')

        if self.max_players and self.min_players:
            if self.max_players < self.min_players:
                raise ValidationError('Max players is less than min players')


class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
