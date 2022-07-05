from django.db import models
from django_jsonform.models.fields import JSONField

from globalapp.model_schemes import SETTINGS_DATA


# Regions
class Region(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    abbr = models.CharField(max_length=10, blank=True)
    # image --->> https://www.countryflags.io/<country_code>/flat/64.png

    class Meta:
        db_table = "glob_regions"
        verbose_name = "Region"
        verbose_name_plural = "Regions"
        ordering = ["name"]

    def __str__(self):
        return self.name


# Countries
class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    abbr = models.CharField(max_length=10, blank=True)
    # image --->> https://www.countryflags.io/<country_code>/flat/64.png
    continent = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "glob_countries"
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["name"]

    def __str__(self):
        return self.name


# Organizers
class Organizer(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    # logo -- pending
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "glob_organizers"
        verbose_name = "Organizer"
        verbose_name_plural = "Organizers"
        ordering = ["name"]

    def __str__(self):
        return self.name


# Player Settings
class PlayerSetting(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    settings_data = JSONField(blank=True, schema=SETTINGS_DATA)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "glob_player_settings"
        verbose_name = "Player Setting"
        verbose_name_plural = "Player Settings"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title
