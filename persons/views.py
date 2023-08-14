from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from persons.models import Person


# Create your views here.
def index_view(request):
    return HttpResponse("<h1>Hello World</h1>")


def person_detail_view(request, person_id):
    try:
        person_object = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        return JsonResponse({"error": "Not Found", "message": "person not found"})
    return JsonResponse({
        "id": person_object.id,
        "name": person_object.name,
        "age": person_object.age
    })
