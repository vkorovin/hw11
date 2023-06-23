from typing import Optional, Tuple
from django.db.models import QuerySet
from server.apps.mytodo.logic.todos import commands, queries, validation
from server.apps.mytodo.models import MyToDo

def run(id:int) -> None:
    commands.delete(id)

