from django.test import TestCase

from games.forms import GameForm


class GameFormTest(TestCase):
    def test_valid_data(self):
        form = GameForm({
            'location': 'Roble Field',
            'datetime': '2019-12-03',
            'max_players': 12,
            'min_players': 10,
        })

        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = GameForm({})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'location': ['This field is required.'],
            'datetime': ['This field is required.'],
            'max_players': ['This field is required.'],
            'min_players': ['This field is required.'],
        })
