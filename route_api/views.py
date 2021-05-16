import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from route_api.models import Routes
from route_api.route_finder import find_best_path


@require_http_methods(["GET"])
def route(request):
    """
    Requires query params ?from:xxx&to=yyy
    where xxx, yyy are integers (as strings in the querysting)
    """
    params = request.GET
    if not ('from' in params and 'to' in params):
        return HttpResponseBadRequest("Missing From or To query params eg ?from:1&to=2")
    try:
        node_from = int(params['from'])
        node_to = int(params['to'])
    except ValueError as e:
        return HttpResponseBadRequest(f"From or To query params are not integers: {params['from']}:{params['to']}")

    best_path = find_best_path(node_from, node_to)

    return HttpResponse(json.dumps(best_path))