from typing import Optional, Tuple

from django.db.models import QuerySet

from server.apps.mytodo.logic.todos import commands, queries, validation
from server.apps.mytodo.models import MyToDo


def run(
    title: Optional[str],
    description: Optional[str],
    is_done: Optional[bool],
) -> Tuple[bool, QuerySet[MyToDo]]:
    """Validates data, maybe creates a new post, returns all published ones."""
    validated_data = validation.validate(
        title=title,
        description=description,
        is_done=is_done,
    )
    if validated_data:
        commands.create(validated_data)

    todos = queries.list_notdeleted()
    return validated_data is not None, todos
