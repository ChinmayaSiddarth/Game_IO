# Generated by Django 3.1.3 on 2020-11-27 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamer_zone', '0003_auto_20201128_0111'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drinks',
            new_name='Drink',
        ),
        migrations.RenameModel(
            old_name='Indoor_Games',
            new_name='Indoor_Game',
        ),
        migrations.RenameModel(
            old_name='Outdoor_Games',
            new_name='Outdoor_Game',
        ),
    ]
