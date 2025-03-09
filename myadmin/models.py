from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    ar_time = models.TimeField()
    ld_time = models.TimeField()
    de_time = models.TimeField()
    experience = models.IntegerField()
    age = models.IntegerField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name
