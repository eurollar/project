from django.urls import path
from room import views

urlpatterns = [
    path('room/<int:room_id>/', views.room, name='room-detail'),
    path('', views.main_page),
]
