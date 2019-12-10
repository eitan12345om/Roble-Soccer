from django.db import models


class Game(models.Model):
    DEFAULT_NUM_PLAYERS = 18

    location = models.CharField(max_length=100, default='Roble Field')
    datetime = models.DateTimeField('when')
    max_players = models.PositiveSmallIntegerField(default=DEFAULT_NUM_PLAYERS)

    def __str__(self):
        return f'Game at {self.location} on {self.datetime}'


class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    opted_for_waitlist = models.BooleanField('Start on Waitlist', default=False)

    def __str__(self):
        return f'{self.name}'
