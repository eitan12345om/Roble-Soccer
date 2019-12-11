from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from games.models import Game


class Command(BaseCommand):
    help = 'Cleans the database'
    MAX_AGE_IN_WEEKS = 4

    def add_arguments(self, parser):
        parser.add_argument('max_age', nargs='?', type=int, default=4)

    def handle(self, *args, **options):
        max_age = options.get('max_age', Command.MAX_AGE_IN_WEEKS)
        weeks_ago = datetime.today() - timedelta(weeks=max_age)

        Game.objects.filter(datetime__lt=weeks_ago).delete()
