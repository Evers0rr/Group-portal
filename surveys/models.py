from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SurveyQuestion(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.order + 1}. {self.text}"

class SurveyAnswer(models.Model):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now=True)

class SurveyResponseAnswer(models.Model):
    response = models.ForeignKey(SurveyResponse, on_delete=models.CASCADE, related_name='response_answers')
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    answer = models.ForeignKey(SurveyAnswer, on_delete=models.CASCADE)

class SurveyChoice(models.Model):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text