# Generated by Django 4.0.6 on 2022-08-07 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_shop_slug_name_remove_shop_slug_town'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug_author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='slug_isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='slug_publication',
        ),
        migrations.RemoveField(
            model_name='book',
            name='slug_title',
        ),
    ]
