from django.urls import path
from .views import (
    CustomUserAPIView, AgentAPIView, DriverAPIView, CriteriaAPIView, AlmondAPIView,
    ControlPointAPIView, ControlPointByAgentAPIView, RoadControlAPIView, 
    CriteriaByControlAPIView, VehicleAPIView,
)

app_name="api"

urlpatterns = [
    path('customusers/', CustomUserAPIView.as_view(), name='customuser-list'),
    path('customusers/<int:pk>/', CustomUserAPIView.as_view(), name='customuser-detail'),
    
    path('agents/', AgentAPIView.as_view(), name='agent-list'),
    path('agents/<int:pk>/', AgentAPIView.as_view(), name='agent-detail'),

    path('drivers/', DriverAPIView.as_view(), name='driver-list'),
    path('drivers/<int:pk>/', DriverAPIView.as_view(), name='driver-detail'),

    path('criteria/', CriteriaAPIView.as_view(), name='criteria-list'),
    path('criteria/<int:pk>/', CriteriaAPIView.as_view(), name='criteria-detail'),

    path('almonds/', AlmondAPIView.as_view(), name='almond-list'),
    path('almonds/<int:pk>/', AlmondAPIView.as_view(), name='almond-detail'),

    path('controlpoints/', ControlPointAPIView.as_view(), name='controlpoint-list'),
    path('controlpoints/<int:pk>/', ControlPointAPIView.as_view(), name='controlpoint-detail'),

    path('controlpointsbyagent/', ControlPointByAgentAPIView.as_view(), name='controlpointbyagent-list'),
    path('controlpointsbyagent/<int:pk>/', ControlPointByAgentAPIView.as_view(), name='controlpointbyagent-detail'),

    path('roadcontrols/', RoadControlAPIView.as_view(), name='roadcontrol-list'),
    path('roadcontrols/<int:pk>/', RoadControlAPIView.as_view(), name='roadcontrol-detail'),

    path('criteriabycontrol/', CriteriaByControlAPIView.as_view(), name='criteriabycontrol-list'),
    path('criteriabycontrol/<int:pk>/', CriteriaByControlAPIView.as_view(), name='criteriabycontrol-detail'),

    path('vehicles/', VehicleAPIView.as_view(), name='vehicle-list'),
    path('vehicles/<int:pk>/', VehicleAPIView.as_view(), name='vehicle-detail'),
]

