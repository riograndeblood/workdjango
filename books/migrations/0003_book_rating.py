# Generated by Django 4.2.1 on 2023-05-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
