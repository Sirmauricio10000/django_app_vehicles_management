import uuid
from django.db import models

class AssignmentLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle_license_plate = models.CharField(max_length=10)
    route_name = models.CharField(max_length=100)
    assignment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log {self.vehicle_license_plate} - {self.route_name} ({self.assignment_date})"
