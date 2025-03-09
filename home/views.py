from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Rendering index.html

def departments(request):
    return render(request, 'departments/departments.html')  # Rendering departments.html

# def department_detail(request, department_name):
#     return render(request, f'departments/{department_name}.html')  # Dynamic rendering
