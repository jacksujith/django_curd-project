from django.contrib import admin
from django.urls import path
from blogapps import views


urlpatterns = [
     path('',views.index),
     path('delete/<int:id>',views.delete,name="delete"),
     path('update/<int:id>',views.update,name="update"),
     path('create/',views.create),
     
]
