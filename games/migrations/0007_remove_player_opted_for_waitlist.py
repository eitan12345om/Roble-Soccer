# Generated by Django 3.0.2 on 2020-01-12 02:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('games', '0006_game_min_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='opted_for_waitlist',
        ),
    ]