from django.urls import path
from room import views

urlpatterns = [
    path('room/', views.room),
    path('', views.main_page),
]
