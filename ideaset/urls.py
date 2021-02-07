from django.urls import path
from .views import index,edit,remove

urlpatterns = [
   path('', index , name='index'),
   path('edit/<int:id>/', edit , name='edit'),
   path('remove/<int:id>/',remove , name='remove'),

]
