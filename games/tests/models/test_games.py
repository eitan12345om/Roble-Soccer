from django.test import TestCase

from games.models import Game


class GameModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.game = Game.objects.create(datetime="2019-12-03 00:00:00-08")

    def test_str(self):
        self.assertEqual(str(self.game),
                         f"Game at {self.game.location} on {self.game.datetime}")
