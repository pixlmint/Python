# Generated by Django 2.1.4 on 2019-02-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_game_wort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerword',
            name='word',
            field=models.CharField(max_length=100),
        ),
    ]