# Generated by Django 4.0.6 on 2022-07-05 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('csgo', '0002_cseventtier_avatar_cseventtype_avatar_csmap_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='csplayer',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cstournament',
            name='cover_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
