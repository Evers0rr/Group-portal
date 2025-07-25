from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.user.email}'
    
class Subjects(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Subjects'
        verbose_name = 'Subject'

    def __str__(self):
        return self.name
  
class Grade(models.Model):
    student = models.ForeignKey('Student',on_delete=models.CASCADE, related_name='grades')
    subjects = models.ForeignKey('Subjects',on_delete=models.CASCADE, related_name='grades')
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    date = models.DateField()

    def __str__(self):
        return f'Студент{self.student} отримав по предмету: {self.subjects} - {self.value}'
    
    
    

