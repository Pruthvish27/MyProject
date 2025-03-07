from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, DoctorViewSet, AvailabilityViewSet

router = DefaultRouter()
router.register(r'department', DepartmentViewSet)  # Only Emergency
router.register(r'doctors', DoctorViewSet)
router.register(r'availability', AvailabilityViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
