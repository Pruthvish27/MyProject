from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, DoctorViewSet, AvailabilityViewSet

router = DefaultRouter()
router.register(r'department', DepartmentViewSet)  # Only Emergency
router.register(r'doctors', DoctorViewSet)
router.register(r'availability', AvailabilityViewSet)

# Function to redirect from "/" to "/api/"
def redirect_to_api(request):
    return redirect('/api/')

urlpatterns = [
    path('', redirect_to_api),  # Redirect root to /api/
    path('api/', include(router.urls)),
]
