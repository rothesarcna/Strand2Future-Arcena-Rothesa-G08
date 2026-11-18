
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentProfile


class StudentRegistrationForm(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    school_name = forms.CharField(max_length=150)

    grade_level = forms.ChoiceField(
        choices=StudentProfile.GRADE_CHOICES
    )

    strand = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'school_name',
            'grade_level',
            'strand',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'This email address is already registered.'
            )

        return email

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

            StudentProfile.objects.create(
                user=user,
                school_name=self.cleaned_data['school_name'],
                grade_level=self.cleaned_data['grade_level'],
                strand=self.cleaned_data['strand']
            )

        return user


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(
            email__iexact=email
        ).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                'This email address is already in use.'
            )

        return email


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile
        fields = [
            'school_name',
            'grade_level',
            'strand',
        ]
