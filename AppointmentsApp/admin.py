from django.contrib import admin

from .models import Appointment, status


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "doctor", "patient", "appointment_date", "duration", "status")
    list_filter = ("status", "doctor", "appointment_date")
    search_fields = (
        "doctor__last_name",
        "patient__last_name",
        "patient__id_national",
        "reason",
    )
    date_hierarchy = "appointment_date"
    ordering = ("appointment_date",)
    readonly_fields = ("created_at", "updated_at")
    actions = ["confirm_appointments", "cancel_appointments"]

    @admin.action(description="Mark selected appointments as Confirmed")
    def confirm_appointments(self, request, queryset):
        queryset.update(status=status.CONFIRMED)

    @admin.action(description="Mark selected appointments as Cancelled")
    def cancel_appointments(self, request, queryset):
        queryset.update(status=status.CANCELED)