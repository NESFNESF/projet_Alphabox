from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='user_interface'),
    path('menu', views.menu_one , name='menu_one'),
    path('configuration' , views.configuration , name="configuration"), 
    path('config' ,views.config , name="config"),
    path('part_one' , views.part_one , name="part_one")
]