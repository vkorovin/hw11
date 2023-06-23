from django.db.models import QuerySet
from server.apps.mytodo.models import MyToDo


def list_notdeleted() -> QuerySet[MyToDo]:
    """Returns all not deleted."""
    return MyToDo.objects.filter().order_by('created_at')

def find_id(id:int) -> QuerySet[MyToDo]:
    return MyToDo.objects.filter(id = id)
