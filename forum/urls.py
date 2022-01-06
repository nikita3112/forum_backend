from django import urls
from django.urls import path
from .views import CreateMessage, CreateTheme, CreateThread

urlpatterns = [
    path('create_message', CreateMessage.as_view()),
    path('create_theme', CreateTheme.as_view()),
    path('create_thread', CreateThread.as_view())
]
