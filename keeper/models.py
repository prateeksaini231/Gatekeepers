from django.db import models
import json

# Create your models here.

class Visitors(models.Model):
    name = models.CharField(max_length = 20)
    houseno = models.CharField(max_length = 10)
    purpose = models.CharField(max_length = 10)
    date_time = models.DateTimeField('visit_date_time')

