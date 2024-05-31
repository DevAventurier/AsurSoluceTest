from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Agent, Driver, Criteria, Almond, ControlPoint, ControlPointByAgent, RoadControl, CriteriaByControl, Vehicle
from .serializers import CustomUserSerializer, AgentSerializer, DriverSerializer, CriteriaSerializer, AlmondSerializer, ControlPointSerializer, ControlPointByAgentSerializer, RoadControlSerializer, CriteriaByControlSerializer, VehicleSerializer
from datetime import datetime

class CustomUserAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            custom_user = CustomUser.objects.get(pk=pk)
            serializer = CustomUserSerializer(custom_user)
        else:
            custom_users = CustomUser.objects.all()
            serializer = CustomUserSerializer(custom_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        custom_user = CustomUser.objects.get(pk=pk)
        serializer = CustomUserSerializer(custom_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        custom_user = CustomUser.objects.get(pk=pk)
        custom_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AgentAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            agent = Agent.objects.get(pk=pk)
            serializer = AgentSerializer(agent)
        else:
            agents = Agent.objects.all()
            serializer = AgentSerializer(agents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        agent = Agent.objects.get(pk=pk)
        serializer = AgentSerializer(agent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        agent = Agent.objects.get(pk=pk)
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DriverAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            driver = Driver.objects.get(pk=pk)
            serializer = DriverSerializer(driver)
        else:
            drivers = Driver.objects.all()
            serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        driver = Driver.objects.get(pk=pk)
        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        driver = Driver.objects.get(pk=pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CriteriaAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            criteria = Criteria.objects.get(pk=pk)
            serializer = CriteriaSerializer(criteria)
        else:
            criterias = Criteria.objects.all()
            serializer = CriteriaSerializer(criterias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CriteriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        criteria = Criteria.objects.get(pk=pk)
        serializer = CriteriaSerializer(criteria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        criteria = Criteria.objects.get(pk=pk)
        criteria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AlmondAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            almond = Almond.objects.get(pk=pk)
            serializer = AlmondSerializer(almond)
        else:
            almonds = Almond.objects.all()
            serializer = AlmondSerializer(almonds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlmondSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        almond = Almond.objects.get(pk=pk)
        serializer = AlmondSerializer(almond, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        almond = Almond.objects.get(pk=pk)
        almond.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ControlPointAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            control_point = ControlPoint.objects.get(pk=pk)
            serializer = ControlPointSerializer(control_point)
        else:
            control_points = ControlPoint.objects.all()
            serializer = ControlPointSerializer(control_points, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ControlPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        control_point = ControlPoint.objects.get(pk=pk)
        serializer = ControlPointSerializer(control_point, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        control_point = ControlPoint.objects.get(pk=pk)
        control_point.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ControlPointByAgentAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            control_point_by_agent = ControlPointByAgent.objects.get(pk=pk)
            serializer = ControlPointByAgentSerializer(control_point_by_agent)
        else:
            control_points_by_agent = ControlPointByAgent.objects.all()
            serializer = ControlPointByAgentSerializer(control_points_by_agent, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ControlPointByAgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        control_point_by_agent = ControlPointByAgent.objects.get(pk=pk)
        serializer = ControlPointByAgentSerializer(control_point_by_agent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        control_point_by_agent = ControlPointByAgent.objects.get(pk=pk)
        control_point_by_agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RoadControlAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            road_control = RoadControl.objects.get(pk=pk)
            serializer = RoadControlSerializer(road_control)
        else:
            road_controls = RoadControl.objects.all()
            serializer = RoadControlSerializer(road_controls, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoadControlSerializer(data=request.data)
      
        data = request.data
        date_str = data['date']
        controlPointId = data['controlPoint']['id']
        agentId = data['agent']['id']
        critera_check = data['critera_check']
        
        control_point = ControlPoint.objects.filter(id=controlPointId).first()
        agent = Agent.objects.filter(id=agentId).first()
        
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f").date().isoformat() 
        roadControl = RoadControl.objects.create(
            date=date,
            control_point=control_point,
            agent=agent,
        )
        
        criteras = Criteria.objects.all()
        for critera in criteras:
            
            state = True if critera.id in critera_check else False
            
            critera_by_control = CriteriaByControl.objects.create(
                criteria=critera,
                road_control=roadControl,
                state=state,
            )
        
        
        return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        #RoadControl()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        road_control = RoadControl.objects.get(pk=pk)
        serializer = RoadControlSerializer(road_control, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        road_control = RoadControl.objects.get(pk=pk)
        road_control.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CriteriaByControlAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            criteria_by_control = CriteriaByControl.objects.get(pk=pk)
            serializer = CriteriaByControlSerializer(criteria_by_control)
        else:
            criterias_by_control = CriteriaByControl.objects.all()
            serializer = CriteriaByControlSerializer(criterias_by_control, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CriteriaByControlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        criteria_by_control = CriteriaByControl.objects.get(pk=pk)
        serializer = CriteriaByControlSerializer(criteria_by_control, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        criteria_by_control = CriteriaByControl.objects.get(pk=pk)
        criteria_by_control.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VehicleAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            vehicle = Vehicle.objects.get(pk=pk)
            serializer = VehicleSerializer(vehicle)
        else:
            vehicles = Vehicle.objects.all()
            serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
