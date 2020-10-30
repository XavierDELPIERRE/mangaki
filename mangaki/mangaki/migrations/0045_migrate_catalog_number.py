# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-10 20:15
from __future__ import unicode_literals

from django.db import migrations, models


def move_catalog_number_to_work(apps, schema_editor):
    Album = apps.get_model("mangaki", "Album")

    # The catalog_number field is now in the Work base class, while the deprecated_catalog_number
    # is in the two derived classes and contains the value of interest.
    for album in Album.objects.all():
        album.catalog_number = album.deprecated_catalog_number
        album.save()


def move_catalog_number_from_work(apps, schema_editor):
    Album = apps.get_model("mangaki", "Album")

    for album in Album.objects.all():
        album.deprecated_catalog_number = album.catalog_number
        album.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0044_migrate_album_composer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='catalog_number',
            new_name='deprecated_catalog_number',
        ),
        migrations.AddField(
            model_name='work',
            name='catalog_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.RunPython(move_catalog_number_to_work, reverse_code=move_catalog_number_from_work),
    ]
