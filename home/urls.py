from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Home Page
    path('departments/', views.departments, name='departments'),  # Departments Overview
    path('room_info/', views.room_info, name='room_info'),  # room_info
    path('report_mapping/', views.report_mapping, name='report_mapping'),  # report_mapping
]
