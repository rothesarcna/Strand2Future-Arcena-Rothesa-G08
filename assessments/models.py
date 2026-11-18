
from django.conf import settings
from django.db import models


class AssessmentQuestion(models.Model):
    question_text = models.TextField()
    category = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text


class QuestionOption(models.Model):
    question = models.ForeignKey(
        AssessmentQuestion,
        on_delete=models.CASCADE,
        related_name='options'
    )
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text


class OptionCourseScore(models.Model):
    option = models.ForeignKey(
        QuestionOption,
        on_delete=models.CASCADE,
        related_name='course_scores'
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='option_scores'
    )
    score = models.PositiveSmallIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['option', 'course'],
                name='unique_option_course_score'
            )
        ]

    def __str__(self):
        return f"{self.option} - {self.course}: {self.score}"


class AssessmentAttempt(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assessment_attempts'
    )
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - Attempt {self.id}"


class AttemptAnswer(models.Model):
    attempt = models.ForeignKey(
        AssessmentAttempt,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    question = models.ForeignKey(
        AssessmentQuestion,
        on_delete=models.CASCADE
    )
    selected_option = models.ForeignKey(
        QuestionOption,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['attempt', 'question'],
                name='unique_attempt_question'
            )
        ]

    def __str__(self):
        return f"{self.attempt} - {self.question}"
