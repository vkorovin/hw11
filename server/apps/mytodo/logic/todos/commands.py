from server.apps.mytodo.logic.todos.validation import ValidToDoData
from server.apps.mytodo.models import MyToDo

def create(valid_data: ValidToDoData) -> MyToDo:
    return MyToDo.objects.create(
        title=valid_data.title,
        description=valid_data.description,
        is_done=valid_data.is_done,
    )
