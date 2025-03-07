from django.db import models

# Emergency Department Model
class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Doctor Model (for Emergency Department)
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    contact = models.CharField(max_length=20, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors')

    def __str__(self):
        return f"{self.name} ({self.specialization})"

# Doctor Availability Model
class Availability(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE, related_name='availability')
    is_available = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.doctor.name} - {'Available' if self.is_available else 'Not Available'}"
