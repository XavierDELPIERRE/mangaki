# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-10 19:53
from __future__ import unicode_literals

from django.db import migrations, models


def move_vo_title_to_work(apps, schema_editor):
    Manga = apps.get_model("mangaki", "Manga")

    # The vo_title field is now in the Work base class, while the deprecated_vo_title
    # is in the two derived classes and contains the value of interest.
    for manga in Manga.objects.all():
        manga.vo_title = manga.deprecated_vo_title
        manga.save()


def move_vo_title_from_work(apps, schema_editor):
    Manga = apps.get_model("mangaki", "Manga")

    for manga in Manga.objects.all():
        manga.deprecated_vo_title = manga.vo_title
        manga.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0041_auto_20160410_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='vo_title',
            new_name='deprecated_vo_title',
        ),
        migrations.AddField(
            model_name='work',
            name='vo_title',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.RunPython(move_vo_title_to_work, reverse_code=move_vo_title_from_work),
    ]
