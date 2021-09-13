#from django.db import models
from djongo import models
# Create your models here.


class Todo(models.Model):
    date=models.DateField()
    content=models.CharField(max_length=200)





