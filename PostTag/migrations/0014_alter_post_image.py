# Generated by Django 4.2.1 on 2023-06-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostTag', '0013_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
