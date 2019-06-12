from django.db import models
from django.contrib.auth.models import User
# Create your models here.
SUBJECT_CHOICES = [
    ('MATHS','MATHS'),
    ('SCIENCE','SCIENCE')
]
class Subject(models.Model):
   
    name = models.CharField(max_length = 100)
    link = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 10,choices = SUBJECT_CHOICES,default = '')

    def __str__(self):
        return str(self.name)