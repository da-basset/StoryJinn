from django.contrib import admin
from .models import prompts, reading_levels

# Register your models here.
admin.site.register(prompts)
admin.site.register(reading_levels)