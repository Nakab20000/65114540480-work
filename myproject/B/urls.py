from django.urls import path
from .views import search_courses

urlpatterns = [
    path('search/', search_courses, name='search_courses'),
    path('', search_courses, name='search_courses'),
]
