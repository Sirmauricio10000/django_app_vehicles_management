import uuid
from django.db import models

class Route(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ROUTE_TYPE_CHOICES = [
        ('Paved', 'Paved'),
        ('Paved with Potholes', 'Paved with Potholes'),
        ('Dirt', 'Dirt'),
        ('Trail', 'Trail'),
    ]
    
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    route_type = models.CharField(max_length=20, choices=ROUTE_TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.origin} - {self.destination})"
