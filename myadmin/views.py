from django.shortcuts import render,redirect
from .models import Doctor
from .forms import DoctorForm

# Create your views here.

def doctor_list(request):
    doctors = Doctor.objects.all()  # Fetch all doctors from the database
    return render(request, 'doctors.html', {'doctors': doctors})


def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')  # Redirect to the doctor list page
    else:
        form = DoctorForm()
    
    return render(request, 'add_doctor.html', {'form': form})
