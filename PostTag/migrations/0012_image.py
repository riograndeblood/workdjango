# Generated by Django 4.2.1 on 2023-06-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostTag', '0011_alter_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
