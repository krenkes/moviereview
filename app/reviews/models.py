from django.db import models

# Create your models here.

class Review(models.Model):
    id = models.CharField(max_length=10, primary_key=True, blank=False, default='')
    title = models.CharField(max_length=70, blank=False, default='')
    industry_rating = models.CharField(max_length=10, blank=False, default='')
    theater_release_year = models.CharField(max_length=10, blank=True, null=True)
    home_release_year = models.CharField(max_length=10, blank=False, default='')
    heavy_lang_index = models.CharField(max_length=100, blank=False, default='')

class Movie(models.Model):
    id = models.CharField(max_length=10, primary_key=True, blank=False, default='')
    title = models.CharField(max_length=70, blank=False, default='')
    industry_rating = models.CharField(max_length=10, blank=False, default='')
    theater_release_year = models.CharField(max_length=10, blank=True, null=True)
    home_release_year = models.CharField(max_length=10, blank=False, default='')
    heavy_lang_index = models.CharField(max_length=100, blank=False, default='')
    light_lang_index = models.CharField(max_length=100, blank=False, default='')
    racial_lang_index = models.CharField(max_length=100, blank=False, default='')

# light_lang_index, religious_lang_index, racial_lang_index