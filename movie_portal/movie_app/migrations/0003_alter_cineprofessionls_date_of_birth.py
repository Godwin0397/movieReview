# Generated by Django 4.2.16 on 2024-09-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_movie_cineprofessionls_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cineprofessionls',
            name='date_of_birth',
            field=models.DateField(auto_now_add=True),
        ),
    ]
