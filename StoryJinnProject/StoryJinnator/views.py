from django.http import HttpResponse
from .models import reading_prompt
from django.template import loader


def index(request):
    template = loader.get_template("StoryJinnator/index.html")
    return HttpResponse(template.render())


def prompts_details(request, reading_prompt):
    return HttpResponse("You're looking at prompt id: %s" % reading_prompt)


def reading_level_details(request, reading_level):
    return HttpResponse("You're looking at reading level: %s" % reading_level)
