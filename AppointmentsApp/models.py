from django.db import models

# Create your models here.
class status(models.TextChoices):
    PENDING = 'Pending','Pending'
    CONFIRMED = 'Confirmed','Confirmed'
    CANCELED = 'Canceled','Canceled'
class Appointment(models.Model):
    reason = models.TextField()
    appointment_date = models.DateField()
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=status.choices,default=status.PENDING)
    doctor = models.ForeignKey('AccountsApp.Doctor',on_delete=models.CASCADE)
    patient = models.ForeignKey('AccountsApp.Patient',on_delete=models.CASCADE)