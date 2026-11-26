from django.urls import path
from . import views

urlpatterns = [
    path("", views.AppointmentListView.as_view(), name="appointment_list"),
    path("new/", views.AppointmentCreateView.as_view(), name="appointment_create"),
    path("<int:pk>/", views.AppointmentDetailView.as_view(), name="appointment_detail"),
    path("<int:pk>/edit/", views.AppointmentUpdateView.as_view(), name="appointment_update"),
]