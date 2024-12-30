from django.shortcuts import render
from django.urls import path
from rest_framework import viewsets
from .models import Patient, Doctor, Appointment
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.cache import cache

def get_patient_data(request, patient_id):
    cache_key = f"patient_{patient_id}"
    patient_data = cache.get(cache_key)

    if not patient_data:
        patient_data = Patient.objects.get(id=patient_id)
        cache.set(cache_key, patient_data, timeout=60*15)

    return render(request, 'patient_detail.html', {'patient': patient_data})

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
