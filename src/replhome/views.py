import json

from django.core import serializers
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from visits.models import Visit

def home_page_view(request, *args, **kwargs):
    queryset = Visit.objects.filter(path=request.path)
    my_title = "Hello Django"

    my_context = {
        "page_title": my_title,
        "queryset": queryset.count(),
    }

    Visit.objects.create(
        path=request.path
    )

    # return HttpResponse(json.dumps(queryset), content_type="application/json")
    return render(request, template_name="home.html", context=my_context)