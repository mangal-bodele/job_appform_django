from django.db import models

class Job(models.Model):
    GENDER = [('F','Female'),('M','Male'),('O','Other')]
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    mobile_number = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=10,choices=GENDER)
    job_title = models.CharField(max_length=10)
    experience = models.CharField(max_length=10)

