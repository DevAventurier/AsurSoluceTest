from django.urls import path
from .views import (
    homeViews
)

app_name="web"

urlpatterns = [
    path('', view=homeViews.dashboard, name='dashbord'),
]

