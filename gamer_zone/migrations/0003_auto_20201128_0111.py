# Generated by Django 3.1.3 on 2020-11-27 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamer_zone', '0002_remove_food_serial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Drink_Name', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Indoor_Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Game_Name', models.CharField(max_length=100)),
                ('Price_per_hour', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Outdoor_Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Game_Name', models.CharField(max_length=100)),
                ('Price_per_hour', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='food',
            name='Drink_Name',
        ),
    ]