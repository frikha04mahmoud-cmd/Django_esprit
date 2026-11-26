from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Doctor


class DoctorListView(ListView):
    model = Doctor
    template_name = "AccountsApp/doctor_list.html"
    context_object_name = "doctors"

    def get_queryset(self):
        qs = Doctor.objects.prefetch_related("specialities").order_by("last_name")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(specialities__name__icontains=q)
        return qs


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = "AccountsApp/doctor_detail.html"
    context_object_name = "doctor"