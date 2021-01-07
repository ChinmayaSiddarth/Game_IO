# Generated by Django 3.1.3 on 2020-11-27 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.IntegerField()),
                ('Food_Name', models.CharField(max_length=100)),
                ('Drink_Name', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
