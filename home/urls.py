from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Home Page
    path("departments/", views.departments, name="departments"),  # Departments Overview
    path("departments/<str:department_name>/", views.department_detail, name="department_detail"),  # Dynamic Department Pages
]
