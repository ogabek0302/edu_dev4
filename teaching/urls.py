from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('group/', views.group, name="group"),
    path('mark/', views.mark, name='mark'),
    # path('delete_students/<int:id>/', views.delete_student, name='delete_student'),
    path('edit_student/<int:id>/', views.edit_student, name='edit_student')
]


