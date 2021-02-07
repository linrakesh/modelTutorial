from django.shortcuts import render,redirect
from .models import Task
# Create your views here.


def index(request):
  if request.user.is_authenticated:
    current_user = request.user
    tasks = Task.objects.all().filter(user__username=current_user.username).order_by('task_priority')
    return render(request, 'ideaset/index.html',{'task_list':tasks})
  else:
    return render(request, 'ideaset/index-blank.html')


def edit(request,id):
  task = Task.objects.get(id=id)
  return render(request,'ideaset/edit.html',{'task':task})

def remove(request,id):
  task = Task.objects.get(id=id)
  task.delete()
  return redirect('/')