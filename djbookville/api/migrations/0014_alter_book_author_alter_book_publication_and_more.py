# Generated by Django 4.0.6 on 2022-08-07 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_book_shop_alter_shop_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.SlugField(),
        ),
    ]