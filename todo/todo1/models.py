from django.db import models
import datetime

# Create your models here.
class alluser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    online = models.CharField(max_length=1,default="n")

class alljob(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.datetime.now())
    content = models.CharField(max_length=50)
    done = models.CharField(max_length=1,default="n")
    name = models.CharField(max_length=10)