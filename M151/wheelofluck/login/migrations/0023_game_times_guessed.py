# Generated by Django 2.1.4 on 2019-02-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0022_game_output'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='times_guessed',
            field=models.IntegerField(default=0),
        ),
    ]