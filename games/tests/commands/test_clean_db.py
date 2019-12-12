from datetime import datetime, timedelta, timezone
from io import StringIO
import pytz

from django.core.management import call_command
from django.test import TestCase

from games.models import Game, Player


class CleanDBTest(TestCase):
    def setUp(self):
        now_game = Game.objects.create(datetime=datetime.now(timezone.utc))
        four_weeks_old_game = Game.objects.create(datetime=datetime.now(timezone.utc) - timedelta(weeks=4))
        five_weeks_old_game = Game.objects.create(datetime=datetime.now(timezone.utc) - timedelta(weeks=5))

        player = Player.objects.create(game=now_game, name="Bob Jones")

    def test_command_output(self):
        out = StringIO()
        call_command('clean_db', stdout=out)

        self.assertIn("Deleted 2 object(s): {'games.Player': 0, 'games.Game': 2}", out.getvalue())

    def test_command_5_weeks(self):
        out = StringIO()
        call_command('clean_db', max_age=5, stdout=out)

        self.assertEquals(len(Game.objects.all()), 2)
