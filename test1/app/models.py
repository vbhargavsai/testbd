from django.db import models

# Create your models here.
class tester(models.Model):
    ctg=models.CharField(max_length=30)
    crs=models.CharField(max_length=30)
    auth=models.CharField(max_length=30)
