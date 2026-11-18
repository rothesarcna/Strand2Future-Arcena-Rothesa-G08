
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150, unique=True)
    abbreviation = models.CharField(max_length=20, blank=True)
    description = models.TextField()
    duration_years = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )

    careers = models.ManyToManyField(
        'Career',
        through='CourseCareer',
        related_name='courses'
    )

    skills = models.ManyToManyField(
        'Skill',
        through='CourseSkill',
        related_name='courses'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subject(models.Model):

    SEMESTER_CHOICES = [
        ('1st Semester', '1st Semester'),
        ('2nd Semester', '2nd Semester'),
        ('Summer', 'Summer'),
    ]

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='subjects'
    )

    subject_code = models.CharField(max_length=20, blank=True)
    subject_name = models.CharField(max_length=150)
    year_level = models.PositiveSmallIntegerField()
    semester = models.CharField(
        max_length=20,
        choices=SEMESTER_CHOICES
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.subject_name


class Career(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CourseCareer(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    career = models.ForeignKey(
        Career,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course', 'career'],
                name='unique_course_career'
            )
        ]

    def __str__(self):
        return f"{self.course.name} - {self.career.title}"


class CourseSkill(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course', 'skill'],
                name='unique_course_skill'
            )
        ]

    def __str__(self):
        return f"{self.course.name} - {self.skill.name}"
