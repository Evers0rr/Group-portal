from django.contrib import admin
from .models import Survey, SurveyQuestion, SurveyChoice, SurveyResponse, SurveyAnswer


admin.site.register(Survey)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyChoice)
admin.site.register(SurveyResponse)
admin.site.register(SurveyAnswer)
