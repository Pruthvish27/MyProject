from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Department, Doctor, Availability
from .serializers import DepartmentSerializer, DoctorSerializer, AvailabilitySerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.filter(name="Emergency Department")  # Only ER Department
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.filter(department__name="Emergency Department")  # Only ER doctors
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.filter(doctor__department__name="Emergency Department")
    serializer_class = AvailabilitySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
