from django.http import HttpResponse
from .models import reading_prompt, reading_level
from django.template import loader


def index(request):
    template = loader.get_template("StoryJinnator/index.html")
    return HttpResponse(template.render())


def prompts_details(request, pid):
    return HttpResponse("You're looking at prompt id: %s" % pid)


def reading_level_details(request, level_id):
    return HttpResponse("You're looking at reading level: %s" % level_id)

