from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
   list_display = ('task_name','task_desc','task_date','user','task_priority')
   list_per_page = 10
   search_fields =('task_name','task_desc')
   list_filter =('task_name','task_date')
   