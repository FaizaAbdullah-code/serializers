from django.db import models

# Create your models here.

class Heros(models.Model):
    name = models.CharField(max_length=60)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class bioData(models.Model):
    name = models.CharField(max_length=60)
    rollno = models.IntegerField()
    section = models.CharField(max_length=1)
    year = models.IntegerField()

    def __str__(self):
        return self.rollno