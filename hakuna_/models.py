from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    age = models.IntegerField(null = True)
    student = models.BooleanField(default=False, null = True)