from django.urls import path

from server.apps.mytodo.views import create, index

app_name = 'mytodo'

urlpatterns = [
    path('create', create, name='create'),
    path('', index, name='list'),
]
