import uuid
from django.db import models
from .route import Route

class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Assigned', 'Assigned'),
        ('In Maintenance', 'In Maintenance'),
    ]

    VEHICLE_TYPE_CHOICES = [
        ('Bus', 'Bus'),
        ('Truck', 'Truck'),
        ('Car', 'Car'),
        ('SUV', 'SUV'),
    ]

    license_plate = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    route_id = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.license_plate} ({self.vehicle_type})"
