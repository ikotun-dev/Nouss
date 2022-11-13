from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [

#    this section is where all urls which would be used in our app is predefined 
#    its called url routing 


    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('addCourses', views.addCourses, name="addCourses"),
    path('addRooms', views.addRooms, name="addRooms"),
    path('addGroup', views.addGroup, name="addGroup"),
    path('addTutor', views.addTutor, name="addTutor"),
    path('genTable', views.genTable, name="genTable"),
    


]
 