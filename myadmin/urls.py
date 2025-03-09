from django.urls import path
from .views import doctor_list,add_doctor

urlpatterns = [
    path('doctors/', doctor_list, name='doctor_list'),
    path('add-doctor/', add_doctor, name='add_doctor'),
]

