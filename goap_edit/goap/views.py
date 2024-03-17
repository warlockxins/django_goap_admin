from django.http import JsonResponse, HttpResponse
from .view_helpers import get_plan_config
from django.template import loader
from .planner.finder import Finder


def index(request, id=0):
    return JsonResponse(get_plan_config(id))


def playground(request, id=0):

    plan = get_plan_config(id)
    template = loader.get_template("goap/index.html")
    context = {
        "id": id,
        "plan": plan
    }

    if request.method == "GET":
        context['result'] = []
        return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        new_world = {}

        for p in plan['world_state']:
            new_world[p] = request.POST.get(p) == 'on'

        context['plan']['world_state'] = new_world
        finder = Finder(context['plan'])
        context['result'] = finder.execute()
        return HttpResponse(template.render(context, request))
