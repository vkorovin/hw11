from django.urls import path

from server.apps.mytodo.views import create, update,  index, delete

app_name = 'mytodo'

urlpatterns = [
    path('create', create, name='create'),
    path('', index, name='list'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete')
]
