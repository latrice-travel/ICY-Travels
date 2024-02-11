from django.urls import path
from trips.views import create_trip, trip_list


urlpatterns = [
    path('create/', create_trip, name="create_trip"),
    path('trips/', trip_list, name="trip_list"),
]
