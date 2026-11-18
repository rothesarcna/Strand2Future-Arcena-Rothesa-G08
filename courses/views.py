
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Course


def course_list(request):
    search_query = request.GET.get('q', '')

    courses = Course.objects.all()

    if search_query:
        courses = courses.filter(
            Q(name__icontains=search_query) |
            Q(abbreviation__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    return render(request, 'courses/course_list.html', {
        'courses': courses,
        'search_query': search_query
    })


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    return render(request, 'courses/course_detail.html', {
        'course': course
    })
