from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Rendering index.html

def departments(request):
    return render(request, 'departments/departments.html')  # Rendering departments.html

def room_info(request):
    return render(request, 'room_info/room_info.html')  # Rendering room_info.html

def report_mapping(request):
    return render(request, 'report_mapping/report_mapping.html')  # Rendering report_mapping.html