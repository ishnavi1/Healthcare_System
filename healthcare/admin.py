from django.contrib import admin
from .models import Patient, Doctor, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'contact_number')
    search_fields = ('user__username', 'contact_number')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty', 'available_from', 'available_to')
    list_filter = ('specialty',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time')