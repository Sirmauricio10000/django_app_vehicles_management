from rest_framework import serializers
from .models import Route, Vehicle, AssignmentLog

class RouteSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Route
        fields = '__all__'

    def validate(self, data):
        """
        Custom validation to ensure that the route type is compatible
        with the assigned vehicle's type.
        """
        route_instance = self.instance
        new_route_type = data.get('route_type', route_instance.route_type if route_instance else None)

        # Si hay un vehículo asignado a la ruta, valida la compatibilidad
        if route_instance and hasattr(route_instance, 'vehicle'):
            vehicle = route_instance.vehicle  # Usa la relación inversa de OneToOneField
            is_valid_assignment = (
                (new_route_type == 'Paved' and vehicle.vehicle_type == 'Bus') or
                (new_route_type == 'Paved with Potholes' and vehicle.vehicle_type == 'Truck') or
                (new_route_type == 'Dirt' and vehicle.vehicle_type == 'Car') or
                (new_route_type == 'Trail' and vehicle.vehicle_type == 'SUV')
            )
            if not is_valid_assignment:
                raise serializers.ValidationError(
                    f"Cannot update route type to '{new_route_type}' because it is not compatible with the assigned vehicle of type '{vehicle.vehicle_type}'."
                )

        return data
    
    def validate_delete(self):
        """
        Custom validation to ensure that a route with an assigned vehicle cannot be deleted.
        """
        if self.instance and hasattr(self.instance, 'vehicle') and self.instance.vehicle is not None:
            raise serializers.ValidationError("This route cannot be deleted because it is assigned to a vehicle.")
        

class VehicleSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Vehicle
        fields = '__all__'

    def validate(self, data):
        """
        Custom validation to ensure that the vehicle type matches the route type and is not re-assigned
        to the same route.
        """
        vehicle_type = data.get('vehicle_type') or self.instance.vehicle_type
        route = data.get('route_id')  # Puede ser None si no se asigna una ruta

        # Verificar si ya está asignado a la misma ruta
        if self.instance and route and self.instance.route_id == route:
            raise serializers.ValidationError(
                "This vehicle is already assigned to the selected route."
            )
        
        # Verificar si la ruta ya está asignada a otro vehículo
        if route is not None and Vehicle.objects.filter(route_id=route).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError(
                {"error": "This route is already assigned to another vehicle."}
            )
        
        if route is None and self.instance.route_id is None:
            raise serializers.ValidationError(
                {"error": "This vehicle is already unassigned from any route."}
            )

        # Si hay una ruta asignada, aplica las validaciones de compatibilidad
        if route is not None:
            is_valid_assignment = (
                (route.route_type == 'Paved' and vehicle_type == 'Bus') or
                (route.route_type == 'Paved with Potholes' and vehicle_type == 'Truck') or
                (route.route_type == 'Dirt' and vehicle_type == 'Car') or
                (route.route_type == 'Trail' and vehicle_type == 'SUV')
            )

            # Si la asignación es inválida, lanza un error de validación
            if not is_valid_assignment:
                raise serializers.ValidationError(
                    f"A vehicle of type '{vehicle_type}' cannot be assigned to a route of type '{route.route_type}'."
                )

        return data

class AssignmentLogSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = AssignmentLog
        fields = '__all__'

    
