# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 18:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('irl', '0001_initial'), ('irl', '0002_auto_20160110_2244'), ('irl', '0003_auto_20160124_1537'), ('irl', '0004_event_attendees'), ('irl', '0003_auto_20160124_1919'), ('irl', '0005_merge'), ('irl', '0006_events_on_work')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mangaki', '0026_auto_20160108_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Titre')),
                ('address', models.TextField(verbose_name='Adresse')),
                ('postal_code', models.CharField(max_length=5, verbose_name='Code postal')),
                ('city', models.CharField(max_length=64, verbose_name='Ville')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('premiere', 'avant-première'), ('screening', 'projection'), ('release', 'sortie'), ('tv', 'diffusion')], max_length=9)),
                ('language', models.CharField(choices=[('vf', 'VF'), ('vostfr', 'VOSTFR'), ('vosta', 'VOSTA')], max_length=6)),
                ('channel', models.CharField(blank=True, default='', max_length=16)),
                ('date', models.DateTimeField()),
                ('link', models.URLField(blank=True, default='')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Work')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='irl.Location')),
            ],
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date']},
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attending', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='irl.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, through='irl.Attendee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=512)),
                ('image', models.CharField(max_length=32, verbose_name='Fichier logo')),
            ],
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'ordering': ['name']},
        ),
    ]
