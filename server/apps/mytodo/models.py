from django.db import models
from typing import Final, final

# Create your models here.
_MYTODO_TITLE_MAX_LENGTH: Final = 60
@final
class MyToDo(models.Model):
    """
    Simple My to do record sved to database
    Fields:
        title - title of todo record.
        description - bodu of nmy to do record
        created_at - date/time of record creation
        upadated_at - date/time of record update

    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_MYTODO_TITLE_MAX_LENGTH)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(auto_created=False)

    objects = models.Manager()

    class Meta(object):
        verbose_name = 'MyToDo'  # You can probably use `gettext` for this
        verbose_name_plural = 'MyToDo'

    def __str__(self) -> str:
        """All django models should have this method."""
        return '<MyToDo: {0}>'.format(self.title)



