from django.shortcuts import render
from .models import Course

def search_courses(request):
    query = request.GET.get('q', '')  # Get search term from the query string
    courses = Course.objects.filter(course_id__icontains=query) if query else Course.objects.all()
    return render(request, 'courses/search.html', {'courses': courses, 'query': query})
