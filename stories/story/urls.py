from django.urls import path
from .views import StoryView


urlpatterns = [
    path('stories/', StoryView.as_view(), name='story-list'),
    path('stories/<int:id>/', StoryView.as_view(), name='story')
]
