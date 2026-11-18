from django.contrib import admin
from .models import (
    AssessmentQuestion,
    QuestionOption,
    OptionCourseScore,
    AssessmentAttempt,
    AttemptAnswer
)

admin.site.register(AssessmentQuestion)
admin.site.register(QuestionOption)
admin.site.register(OptionCourseScore)
admin.site.register(AssessmentAttempt)
admin.site.register(AttemptAnswer)