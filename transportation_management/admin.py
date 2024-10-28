from django.contrib import admin
from .models import Route, Vehicle, AssignmentLog

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'status', 'vehicle_type', 'route_id')

@admin.register(AssignmentLog)
class AssignmentLogAdmin(admin.ModelAdmin):
    list_display = ('vehicle_license_plate', 'route_name', 'assignment_date')

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin', 'destination', 'distance', 'route_type')

