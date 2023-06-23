from django.db.models import QuerySet
from server.apps.mytodo.models import MyToDo


def list_notdeleted() -> QuerySet[MyToDo]:
    """Returns all not deleted."""
    return MyToDo.objects.filter(is_done = False)
