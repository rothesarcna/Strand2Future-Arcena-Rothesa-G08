from django.conf import settings
from django.db import models


class StudentProfile(models.Model):

    GRADE_CHOICES = [
        ('Grade 11', 'Grade 11'),
        ('Grade 12', 'Grade 12'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )

    school_name = models.CharField(max_length=150)
    grade_level = models.CharField(max_length=10, choices=GRADE_CHOICES)
    strand = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username