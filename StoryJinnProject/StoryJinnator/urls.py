from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("prompt/<int:pid>/", views.prompts_details, name="Prompt Details"),
    path("reading_level/<int:level_id>/", views.reading_level_details, name="Reading Level Details")
]