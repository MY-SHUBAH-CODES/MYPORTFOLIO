from django.urls import path,include
from app1 import views



urlpatterns = [
    path('',views.home,name="home"),
    
    ]