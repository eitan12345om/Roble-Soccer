from django.test import TestCase

from games.models import Player, Game


class PlayerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        game = Game.objects.create(datetime="2019-12-03 00:00:00-08")
        cls.player = Player.objects.create(game=game, name="Bob Jones")

    def test_str(self):
        self.assertEqual(str(self.player), self.player.name)
