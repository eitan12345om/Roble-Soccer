import logging
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from games.models import Game

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


class Command(BaseCommand):
    help = 'Cleans the database'
    MAX_AGE_IN_WEEKS = 4

    def add_arguments(self, parser):
        parser.add_argument('max_age', nargs='?', type=int, default=4)

    def handle(self, *args, **options):
        max_age = options.get('max_age', Command.MAX_AGE_IN_WEEKS)
        weeks_ago = datetime.today() - timedelta(weeks=max_age)

        num_objects, objects = Game.objects.filter(
            datetime__lt=weeks_ago).delete()

        logger.info(f"Deleted {num_objects} object(s): {objects}")
        self.stdout.write(
            self.style.SUCCESS(f"Deleted {num_objects} object(s): {objects}"))
