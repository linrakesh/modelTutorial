from django.shortcuts import render,redirect
from .models import Task
# Create your views here.


def index(request):
  if request.user.is_authenticated:
    current_user = request.user
    tasks = Task.objects.all().filter(user__username=current_user.username).order_by('task_priority')
    print(tasks.count())
    if tasks.count()>=1:
      return render(request, 'ideaset/index.html',{'task_list':tasks})
    else:
      return render(request,'ideaset/add_task.html')
  else:
    return render(request, 'ideaset/index-blank.html')


def add(request):
  if request.method == 'POST':
    current_user = request.user
    task_name = request.POST['task_name']
    task_desc = request.POST['task_desc']
    task_date = request.POST['task_date']
    task_priority = request.POST['task_priority']
    task = Task(task_name=task_name,task_desc=task_desc,task_date=task_date,task_priority = task_priority,user=current_user) 
    task.save()
    return redirect('/')
  else:
    return render(request,'ideaset/add_task.html')


def edit(request,id):
  task = Task.objects.get(id=id)
  if request.method =='POST':
    task.task_name = request.POST['task_name']
    task.task_desc = request.POST['task_desc']
    task.task_date = request.POST['task_date']
    task.task_priority = request.POST['task_priority']
    task.save()
    return redirect('/')
  else:
    return render(request,'ideaset/edit.html',{'task':task})


def remove(request,id):
  task = Task.objects.get(id=id)
  task.delete()
  return redirect('/')
