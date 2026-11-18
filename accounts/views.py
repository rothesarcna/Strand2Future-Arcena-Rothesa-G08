
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .forms import (
    StudentRegistrationForm,
    UserProfileForm,
    StudentProfileForm
)
from .models import StudentProfile


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account was created successfully!')
            return redirect('home')
    else:
        form = StudentRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def student_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')


@login_required
def student_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

    return redirect('home')


@login_required
def profile(request):

    student_profile = StudentProfile.objects.get(
        user=request.user
    )

    context = {
        'student_profile': student_profile,
    }

    return render(
        request,
        'accounts/profile.html',
        context
    )


@login_required
@transaction.atomic
def edit_profile(request):

    student_profile = StudentProfile.objects.get(
        user=request.user
    )

    if request.method == 'POST':
        user_form = UserProfileForm(
            request.POST,
            instance=request.user
        )

        student_form = StudentProfileForm(
            request.POST,
            instance=student_profile
        )

        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            student_form.save()

            messages.success(
                request,
                'Your profile was updated successfully!'
            )

            return redirect('profile')

    else:
        user_form = UserProfileForm(instance=request.user)
        student_form = StudentProfileForm(instance=student_profile)

    context = {
        'user_form': user_form,
        'student_form': student_form,
    }

    return render(
        request,
        'accounts/edit_profile.html',
        context
    )
