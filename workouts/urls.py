from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('day/<str:day_name>/', views.day_detail, name='day_detail'),
    path('diet/', views.diet, name='diet'),
]