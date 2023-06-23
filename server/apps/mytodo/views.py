from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from server.apps.mytodo.logic.todos import queries as todo_queries
from server.apps.mytodo.logic.usecases import create_new_todo,update_todo,delete_todo
from server.apps.mytodo.models import MyToDo


# Create your views here.

@require_http_methods(['GET'])
def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """
    todos = todo_queries.list_notdeleted()
    return render(request, 'mytodo/index.html', {'todos': todos})


@require_http_methods(['POST'])
def create(request: HttpRequest) -> HttpResponse:
    """Creates new post if the passed data is valid."""
    is_created, todos = create_new_todo.run(
        title=request.POST.get('title'),
        description=request.POST.get('description'),
        is_done=bool(request.POST.get('is_done')),
    )

    messages.info(request, 'Todo record created: {0}'.format(is_created))
    return redirect(index)

def update(request: HttpRequest,id)-> HttpResponse:
    if request.method == 'GET':
        todo = MyToDo.objects.get(id=id)
        return render(request, 'mytodo/update.html', {'todo': todo})

    if request.method == 'POST':
        is_created, todos = update_todo.run(
        id=id,
        title=request.POST.get('title'),
        description=request.POST.get('description'),
        is_done=bool(request.POST.get('is_done')),
        )
        return redirect(index)
@require_http_methods(['GET'])
def delete(request: HttpRequest,id)-> HttpResponse:
    delete_todo.run(id)
    todos = todo_queries.list_notdeleted()
    return redirect(index)
