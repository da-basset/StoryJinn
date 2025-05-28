from django.contrib import admin
from .models import reading_level, reading_prompt 

# Register your models here.
admin.site.register(reading_level)
admin.site.register(reading_prompt)