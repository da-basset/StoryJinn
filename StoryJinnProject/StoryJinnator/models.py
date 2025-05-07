from django.db import models

class prompt(models.Model):
    id = models.IntegerField
    prompt = models.TextField

class reading_levels(models.Model):
    id = models.IntegerField
    reading_level = models.IntegerField
    prompt = models.TextField
