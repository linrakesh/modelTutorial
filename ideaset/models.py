from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  task_name = models.CharField(max_length=100)
  task_desc = models.CharField(max_length=100)
  task_date  = models.DateField()
  task_priority =models.IntegerField(default=1)
  
  def __str__(self):
    return self.task_name
