# Generated by Django 4.0.6 on 2022-07-04 23:15

from django.db import migrations, models
import django.db.models.deletion
import django_jsonform.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globalapp', '0001_initial'),
        ('commerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=255)),
                ('native_name', models.CharField(blank=True, max_length=255)),
                ('alternate_ids', models.CharField(blank=True, max_length=255)),
                ('born', models.DateField(blank=True, null=True)),
                ('hometown', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('R', 'Retired'), ('U', 'Unknown'), ('M', 'Migrated')], default='A', max_length=1)),
                ('years_active', django_jsonform.models.fields.JSONField(blank=True)),
                ('earnings', models.PositiveIntegerField(blank=True, null=True)),
                ('nicknames', models.CharField(blank=True, max_length=255)),
                ('social_media', django_jsonform.models.fields.JSONField(blank=True)),
                ('team_history', django_jsonform.models.fields.JSONField(blank=True)),
                ('wiki', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', to='globalapp.country')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
                'db_table': 'csgo_players',
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='CsTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('abbr', models.CharField(blank=True, max_length=255)),
                ('hometown', models.CharField(blank=True, max_length=255)),
                ('social_media', django_jsonform.models.fields.JSONField(blank=True)),
                ('staff', django_jsonform.models.fields.JSONField(blank=True)),
                ('wiki', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
                'db_table': 'csgo_teams',
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='EventTier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Event Tier',
                'verbose_name_plural': 'Event Tiers',
                'db_table': 'csgo_event_tiers',
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Event Type',
                'verbose_name_plural': 'Event Types',
                'db_table': 'csgo_event_types',
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('abbr', models.CharField(blank=True, max_length=255)),
                ('wiki', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Map',
                'verbose_name_plural': 'Maps',
                'db_table': 'csgo_maps',
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('team_1_score', models.PositiveIntegerField(default=0)),
                ('team_2_score', models.PositiveIntegerField(default=0)),
                ('start_date_time', models.DateTimeField(blank=True, null=True)),
                ('is_match_finished', models.BooleanField(default=False)),
                ('map_pool', django_jsonform.models.fields.JSONField(blank=True)),
                ('overall_players_stats', django_jsonform.models.fields.JSONField(blank=True, null=True)),
                ('aftermath', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
                'db_table': 'csgo_matches',
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('wiki', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'db_table': 'csgo_roles',
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('abbr', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('venue', models.CharField(blank=True, max_length=255)),
                ('social_media', django_jsonform.models.fields.JSONField(blank=True)),
                ('event_format', models.TextField(blank=True)),
                ('total_matches', models.PositiveIntegerField(default=16)),
                ('match_schedule', django_jsonform.models.fields.JSONField(blank=True)),
                ('total_teams', models.PositiveIntegerField(default=22)),
                ('prize_pool', models.CharField(blank=True, max_length=20)),
                ('prize_distribution', django_jsonform.models.fields.JSONField(blank=True)),
                ('teams_stats', django_jsonform.models.fields.JSONField(blank=True)),
                ('players_stats', django_jsonform.models.fields.JSONField(blank=True)),
                ('broadcasters', django_jsonform.models.fields.JSONField(blank=True)),
                ('talent', django_jsonform.models.fields.JSONField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='globalapp.country')),
                ('event_tier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='csgo.eventtier')),
                ('event_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='csgo.eventtype')),
                ('maps', models.ManyToManyField(blank=True, to='csgo.map')),
                ('organizer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='globalapp.organizer')),
                ('participant_teams', models.ManyToManyField(blank=True, to='csgo.csteam')),
            ],
            options={
                'verbose_name': 'Tournament',
                'verbose_name_plural': 'Tournaments',
                'db_table': 'csgo_tournaments',
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='SingleMapMatch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('team_1_score', models.PositiveIntegerField(default=0)),
                ('team_2_score', models.PositiveIntegerField(default=0)),
                ('map_number', models.PositiveIntegerField(default=1)),
                ('start_date_time', models.DateTimeField(blank=True, null=True)),
                ('is_match_finished', models.BooleanField(default=False)),
                ('players_stats', django_jsonform.models.fields.JSONField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('map', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='csgo.map')),
                ('match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='csgo.match')),
                ('mvp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='csgo.csplayer')),
                ('team_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='single_match_team_1', to='csgo.csteam')),
                ('team_1_players', models.ManyToManyField(blank=True, related_name='team_1_players', to='csgo.csplayer')),
                ('team_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='single_match_team_2', to='csgo.csteam')),
                ('team_2_players', models.ManyToManyField(blank=True, related_name='team_2_players', to='csgo.csplayer')),
            ],
            options={
                'verbose_name': 'Single Map Match',
                'verbose_name_plural': 'Single Map Matches',
                'db_table': 'csgo_single_map_matches',
                'ordering': ['updated_at'],
            },
        ),
        migrations.AddField(
            model_name='match',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='csgo.tournament'),
        ),
        migrations.AddField(
            model_name='match',
            name='mvp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='csgo.csplayer'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_team_1', to='csgo.csteam'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_team_2', to='csgo.csteam'),
        ),
        migrations.AddField(
            model_name='csplayer',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='csgo.role'),
        ),
        migrations.AddField(
            model_name='csplayer',
            name='setup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', to='commerce.pcspec'),
        ),
        migrations.AddField(
            model_name='csplayer',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='csgo.csteam'),
        ),
        migrations.AddField(
            model_name='csplayer',
            name='team_mates',
            field=models.ManyToManyField(blank=True, to='csgo.csplayer'),
        ),
    ]
