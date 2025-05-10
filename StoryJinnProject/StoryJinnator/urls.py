from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("prompt/<int:prompt_id>/", views.prompts_details, name="Prompt Details"),
    path("reading_level/<int:reading_level>/", views.reading_level_details, name="Reading Level Details")
]