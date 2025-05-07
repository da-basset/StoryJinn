from django.db import models

class prompts(models.Model):
    id = models.IntegerField
    text = models.CharField(max_length=200, default="Hello World")

    def __str__(self):
        return self.text

class reading_levels(models.Model):
    id = models.IntegerField
    reading_level = models.IntegerField(default=0)
    text = models.CharField(max_length=200, default="Hello World")

    def __str__(self):
        return self.text
