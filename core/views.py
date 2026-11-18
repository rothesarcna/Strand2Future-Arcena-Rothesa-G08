
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import StudentProfile


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'core/home.html')


@login_required(login_url='/accounts/login/')
def dashboard(request):
    profile = StudentProfile.objects.filter(user=request.user).first()

    return render(request, 'core/dashboard.html', {
        'profile': profile
    })
