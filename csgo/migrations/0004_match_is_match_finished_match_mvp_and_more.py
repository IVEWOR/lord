# Generated by Django 4.0.6 on 2022-07-04 21:19

from django.db import migrations, models
import django.db.models.deletion
import django_jsonform.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('csgo', '0003_eventtier_eventtype_match_singlemapmatch_tournament_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='is_match_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='mvp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='csgo.player'),
        ),
        migrations.AddField(
            model_name='match',
            name='overall_players_stats',
            field=django_jsonform.models.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='start_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
