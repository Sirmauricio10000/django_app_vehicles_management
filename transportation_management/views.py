import json
from .models import Route, Vehicle, AssignmentLog
from .serializers import RouteSerializer, VehicleSerializer, AssignmentLogSerializer
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from django.shortcuts import render

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def destroy(self, request, *args, **kwargs):
        route = self.get_object()
        serializer = self.get_serializer(route)

        # Llama a la validación de eliminación en el serializador
        try:
            serializer.validate_delete()
            route.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except serializers.ValidationError as e:
            return Response({'error': str(e.args[0])}, status=status.HTTP_400_BAD_REQUEST)

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except serializers.ValidationError as e:
            error_messages = []
            for field, messages in serializer.errors.items():
                if isinstance(messages, list):
                    error_messages.extend(messages)
                else:
                    error_messages.append(messages)
            return Response({"error": " ".join(error_messages)}, status=status.HTTP_400_BAD_REQUEST)

class AssignmentLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AssignmentLog.objects.all()
    serializer_class = AssignmentLogSerializer


def vehicle_assign_view(request):
    vehicles = list(Vehicle.objects.values('id', 'license_plate', 'vehicle_type', 'status', 'route_id'))  
    routes = list(Route.objects.values('id', 'name', 'origin', 'destination', 'distance', 'route_type'))  

    # Convertir objetos UUID y Decimal a cadenas para asegurar JSON válido
    for vehicle in vehicles:
        vehicle['id'] = str(vehicle['id'])  # Convertir UUID a cadena
        vehicle['route_id'] = str(vehicle['route_id']) if vehicle['route_id'] else None

    for route in routes:
        route['id'] = str(route['id'])  # Convertir UUID a cadena
        route['distance'] = float(route['distance'])  # Convertir Decimal a float

    # Serializar los datos para enviarlos al frontend
    return render(request, 'transportation_management/vehicle_assign.html', {
        'vehicles': json.dumps(vehicles),
        'routes': json.dumps(routes)
    })

def assignment_log_view(request):
    return render(request, 'transportation_management/assignment_log.html')

def index(request):
    return render(request, 'transportation_management/index.html')
