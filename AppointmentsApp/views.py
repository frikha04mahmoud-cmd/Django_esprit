from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from AccountsApp.models import Doctor, Patient
from .models import Appointment, status

class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = "AppointmentsApp/appointment_list.html"
    context_object_name = "appointments"

    def get_queryset(self):
        qs = Appointment.objects.select_related("doctor", "patient").order_by("appointment_date")
        pk = self.request.user.pk  # Doctor/Patient share the User pk (user_ptr)
        if Patient.objects.filter(pk=pk).exists():
            qs = qs.filter(patient_id=pk)
        elif Doctor.objects.filter(pk=pk).exists():
            qs = qs.filter(doctor_id=pk)
        st = self.request.GET.get("status")
        if st in status.values:
            qs = qs.filter(status=st)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["status_choices"] = status.choices
        return ctx


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = "AppointmentsApp/appointment_detail.html"
    context_object_name = "appointment"


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    """A patient requests an appointment with a doctor."""
    model = Appointment
    fields = ["doctor", "appointment_date", "duration", "reason"]
    template_name = "AppointmentsApp/appointment_form.html"
    success_url = reverse_lazy("appointment_list")

    def form_valid(self, form):
        form.instance.patient = Patient.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)  # status keeps its default: PENDING


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    """A doctor confirms or cancels one of his own appointments."""
    model = Appointment
    fields = ["status"]
    template_name = "AppointmentsApp/appointment_form.html"
    success_url = reverse_lazy("appointment_list")

    def get_queryset(self):
        return Appointment.objects.filter(doctor_id=self.request.user.pk)