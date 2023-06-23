from dataclasses import dataclass
from typing import Optional, final


@final
@dataclass
class ValidToDoData(object):
    """Used to represent valid data that we can use to create a todo record."""

    title: str
    description: str
    is_done: bool


def validate(
    title: Optional[str],
    description: Optional[str],
    is_done: Optional[bool],
) -> Optional[ValidToDoData]:
    """Validates incomming data and decides if we can save it as a post."""
    if not title or not description :
        return None
    return ValidToDoData(title=title, description=description,is_done=is_done)
