# Generated by Django 2.1.4 on 2019-02-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_remove_playerword_assigned_to_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='wort',
            field=models.CharField(max_length=100),
        ),
    ]