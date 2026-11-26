from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Doctor, Patient, Speciality

admin.site.register(User, UserAdmin)


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Doctor)
class DoctorAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "license_number", "phone_number")
    search_fields = ("username", "first_name", "last_name", "license_number")
    list_filter = ("specialities",)
    filter_horizontal = ("groups", "user_permissions", "specialities")

    extra = (("Professional info", {"fields": ("license_number", "phone_number", "specialities")}),)
    fieldsets = UserAdmin.fieldsets + extra
    add_fieldsets = UserAdmin.add_fieldsets + extra

    def get_readonly_fields(self, request, obj=None):
        readonly = list(super().get_readonly_fields(request, obj))
        if obj:  # existing doctor: license number can't change
            readonly.append("license_number")
        return readonly


@admin.register(Patient)
class PatientAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "id_national", "phone_number", "birth_date")
    search_fields = ("username", "first_name", "last_name", "id_national")
    list_filter = ("birth_date",)

    extra = (("Patient info", {"fields": ("id_national", "phone_number", "birth_date")}),)
    fieldsets = UserAdmin.fieldsets + extra
    add_fieldsets = UserAdmin.add_fieldsets + extra

    def get_readonly_fields(self, request, obj=None):
        readonly = list(super().get_readonly_fields(request, obj))
        if obj:
            readonly.append("id_national")
        return readonly