# transportation_management/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'routes', views.RouteViewSet)
router.register(r'vehicles', views.VehicleViewSet)
router.register(r'logs', views.AssignmentLogViewSet)

urlpatterns = [
    # Rutas de la API con prefijo 'api'
    path('api/', include(router.urls)),

    # Rutas directas para las plantillas HTML (sin prefijo)
    path('', views.index, name='index'),
    path('assign/', views.vehicle_assign_view, name='vehicle_assign'),
    path('logs/', views.assignment_log_view, name='assignment_log'),
]