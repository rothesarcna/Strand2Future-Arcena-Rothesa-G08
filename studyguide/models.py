
from django.db import models


class StudyTopic(models.Model):

    STAGE_CHOICES = [
        ('Before College', 'Before College'),
        ('During College', 'During College'),
    ]

    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='study_topics'
    )

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    stage = models.CharField(
        max_length=20,
        choices=STAGE_CHOICES
    )
    year_level = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.course.name} - {self.title}"
