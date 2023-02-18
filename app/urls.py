from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.info, name="info"),
    path('detail/', views.group, name="create_student"),
    path('detail/', views.mark, name='mark'),
    path('detail/', views.course, name='course'),
    path('detail/', views.group, name='group'),

]
