from django.db import models
from django.utils.html import mark_safe
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


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    website = models.URLField()
    facebook_profile = models.URLField()
    twitter_profile = models.URLField()
    photo = models.ImageField(verbose_name='photo',upload_to ='profile/')

    def image_tag(self):
      return mark_safe('<img src ="/media/%s" width="60" height="60"/>' %self.photo )
    
