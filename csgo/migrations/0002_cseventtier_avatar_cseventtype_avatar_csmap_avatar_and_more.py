# Generated by Django 4.0.6 on 2022-07-05 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp', '0002_remove_country_created_at_remove_country_description_and_more'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('csgo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cseventtier',
            name='avatar',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='cseventtype',
            name='avatar',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='csmap',
            name='avatar',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='csmatch',
            name='avatar',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='csplayer',
            name='avatar',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='csrole',
            name='avatar',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='csteam',
            name='logo',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='cstournament',
            name='avatar',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='cstournament',
            name='cover_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cover_image_related', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='csteam',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='globalapp.country'),
        ),
    ]
