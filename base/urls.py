from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tabela/<str:pk>/', views.tabela, name="tabela"),
    path('room/<str:pk>/', views.room, name="room"),
]