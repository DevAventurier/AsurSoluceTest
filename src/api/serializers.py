from rest_framework import serializers
from .models import CustomUser, Agent, Driver, Criteria, Almond, ControlPoint, ControlPointByAgent, RoadControl, CriteriaByControl, Vehicle


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'sexe', 'date_of_birth', 'create_at', 'update_at', 'delete_at', 'user']

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'sexe', 'date_of_birth', 'create_at', 'update_at', 'delete_at', 'user', 'matricule']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        current_control_point = ControlPointByAgent.objects.filter(state=True).first()
        data["current_control_point"] = ControlPointByAgentSerializer(current_control_point).data if current_control_point else {}
        return data

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'sexe', 'date_of_birth', 'create_at', 'update_at', 'delete_at', 'license_number']

class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = ['id', 'name', 'description']

class AlmondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almond
        fields = ['id', 'montant', 'paid']

class ControlPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlPoint
        fields = ['id', 'name', 'gps_location', 'agents']

class ControlPointByAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlPointByAgent
        fields = ['id', 'agent', 'control_point', 'state']

class RoadControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadControl
        fields = ['id', 'date', 'criteria', 'control_point', 'agent']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["control_point"] = ControlPointSerializer(instance.control_point).data
        data["agent"] = AgentSerializer(instance.agent).data
        return data


class CriteriaByControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriteriaByControl
        fields = ['id', 'criteria', 'road_control', 'state', 'almond']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'immatriculation']


