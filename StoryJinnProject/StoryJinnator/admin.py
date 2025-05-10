from django.contrib import admin
from .models import reading_level, reading_prompt #prompts, reading_levels

# Register your models here.
#admin.site.register(prompts)
#admin.site.register(reading_levels)
admin.site.register(reading_level)
admin.site.register(reading_prompt)