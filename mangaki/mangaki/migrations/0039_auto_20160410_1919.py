# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-10 19:19
from __future__ import unicode_literals

from django.db import migrations, models


def move_origin_to_work(apps, schema_editor):
    apps.get_model("mangaki", "Work")
    Anime = apps.get_model("mangaki", "Anime")
    Manga = apps.get_model("mangaki", "Manga")

    # The origin field is now in the Work base class, while the deprecated_origin
    # is in the two derived classes and contains the value of interest.
    for anime in Anime.objects.all():
        anime.origin = anime.deprecated_origin
        anime.save()
    for manga in Manga.objects.all():
        manga.origin = manga.deprecated_origin
        manga.save()


def move_origin_from_work(apps, schema_editor):
    apps.get_model("mangaki", "Work")
    Anime = apps.get_model("mangaki", "Anime")
    Manga = apps.get_model("mangaki", "Manga")

    for anime in Anime.objects.all():
        anime.deprecated_origin = anime.origin
        anime.save()
    for manga in Manga.objects.all():
        manga.deprecated_origin = manga.origin
        manga.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0038_genre_to_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='origin',
            new_name='deprecated_origin',
        ),
        migrations.RenameField(
            model_name='manga',
            old_name='origin',
            new_name='deprecated_origin',
        ),
        migrations.AddField(
            model_name='work',
            name='origin',
            field=models.CharField(blank=True, choices=[('japon', 'Japon'), ('coree', 'Coree'), ('france', 'France'), ('chine', 'Chine'), ('usa', 'USA'), ('allemagne', 'Allemagne'), ('taiwan', 'Taiwan'), ('espagne', 'Espagne'), ('angleterre', 'Angleterre'), ('hong-kong', 'Hong Kong'), ('italie', 'Italie'), ('inconnue', 'Inconnue'), ('intl', 'International')], default='', max_length=10),
        ),
        migrations.RunPython(move_origin_to_work, reverse_code=move_origin_from_work),
    ]
