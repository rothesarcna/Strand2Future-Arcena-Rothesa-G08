from django.contrib import admin
from .models import (
    Course,
    Subject,
    Career,
    Skill,
    CourseCareer,
    CourseSkill
)

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Career)
admin.site.register(Skill)
admin.site.register(CourseCareer)
admin.site.register(CourseSkill)