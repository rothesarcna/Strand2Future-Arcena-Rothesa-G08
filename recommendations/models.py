
from django.conf import settings
from django.db import models


class Recommendation(models.Model):
    attempt = models.ForeignKey(
        'assessments.AssessmentAttempt',
        on_delete=models.CASCADE,
        related_name='recommendations'
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='recommendations'
    )
    score = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField()

    explanation = models.TextField(blank=True)

    class Meta:
        ordering = ['rank']
        constraints = [
            models.UniqueConstraint(
                fields=['attempt', 'course'],
                name='unique_attempt_recommendation'
            )
        ]

    def __str__(self):
        return f"{self.course.name} - Rank {self.rank}"


class SavedCourse(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='saved_courses'
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='saved_by_students'
    )
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'course'],
                name='unique_student_saved_course'
            )
        ]

    def __str__(self):
        return f"{self.student.username} - {self.course.name}"
