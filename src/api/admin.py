from django.contrib import admin
from .models import CustomUser, Agent, Driver, Criteria, Almond, ControlPoint, ControlPointByAgent, RoadControl, CriteriaByControl, Vehicle

# Enregistrement de chaque modèle dans l'administration Django

admin.site.register(CustomUser)
admin.site.register(Agent)
admin.site.register(Driver)
admin.site.register(Criteria)
admin.site.register(Almond)
admin.site.register(ControlPoint)
admin.site.register(ControlPointByAgent)
admin.site.register(RoadControl)
admin.site.register(CriteriaByControl)
admin.site.register(Vehicle)
