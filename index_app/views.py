from django.shortcuts import render
#from index_app import templates


# Create your views here.
def index_page_view(request):
    data={
        "show_data":False,
        "name":"Nihaz",
        "family":"Asar",
        "list":[1,2,3,4,5]
    }
    return render(request, "index.html",context=data)
