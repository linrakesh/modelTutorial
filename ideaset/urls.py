from django.urls import path
from .views import index,edit,remove,add

urlpatterns = [
   path('', index , name='index'),
   path('add/', add , name='add'),
   path('edit/<int:id>/', edit , name='edit'),
   path('remove/<int:id>/',remove , name='remove'),

]
