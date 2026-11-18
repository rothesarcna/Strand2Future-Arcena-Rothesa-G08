
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import StudentProfile
from courses.models import Course
from recommendations.models import SavedCourse
from assessments.models import AssessmentAttempt


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'core/home.html')


@login_required(login_url='/accounts/login/')
def dashboard(request):

    if request.user.is_staff:
        return redirect('admin_dashboard')

    profile = StudentProfile.objects.filter(
        user=request.user
    ).first()

    course_count = Course.objects.count()

    saved_count = SavedCourse.objects.filter(
        student=request.user
    ).count()

    completed_assessments = AssessmentAttempt.objects.filter(
        student=request.user,
        is_completed=True
    ).count()

    context = {
        'profile': profile,
        'course_count': course_count,
        'saved_count': saved_count,
        'completed_assessments': completed_assessments,
    }

    return render(
        request,
        'core/dashboard.html',
        context
    )


@login_required(login_url='/accounts/login/')
def admin_dashboard(request):

    if not request.user.is_staff:
        return redirect('dashboard')

    return render(request, 'core/admin_dashboard.html')
