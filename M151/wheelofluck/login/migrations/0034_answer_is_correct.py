# Generated by Django 2.1.4 on 2019-02-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0033_auto_20190225_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]