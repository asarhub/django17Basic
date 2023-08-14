from django.shortcuts import render, redirect,HttpResponse
from todo_app.models import Todo


# Create your views here.
def list_view(request):
    status_mapping={
        'incomplete':False,'complete':True
    }
    status=request.GET.get("status", "")
    # This is for searching using query params
    search_string = request.GET.get("search", "")
    todo_list = Todo.objects.all().order_by("-created_at")
    print(search_string)
    if search_string != "":
        todo_list = todo_list.filter(title__icontains=search_string)
    if status !="":
        status_in_boolean=status_mapping[status]
        todo_list=todo_list.filter(completed=status_in_boolean)
    data = {
        "todo_list": todo_list
    }
    return render(request, "list.html", context=data)


def update_view(request, todo_id):
    if request.method=="GET":
        return HttpResponse("Error GET not allowed")
    else:
        todo=Todo.objects.get(id=todo_id)
        todo.completed=True
        todo.save()
        return redirect("todo_list_view")


def delete_view(request, todo_id):
    if request.method=="GET":
        return HttpResponse("Error GET not allowed")
    else:
        todo=Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect("todo_list_view")


def create_view(request):
    print("request data")
    todo_title = request.POST["todo_Title"]
    todo_desc = request.POST['todo_Description']
    Todo.objects.create(
        title=todo_title,
        description=todo_desc,
        completed=False
    )
    return redirect("todo_list_view")
    print("todo_Title", "todo_Description", todo_title, todo_desc)
