from django.urls import path
from trips.views import create_trip


urlpatterns = [
    path('trips/', create_trip, name="create_trip"),
]
