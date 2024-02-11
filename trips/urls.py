from django.urls import path
from trips.views import create_trip, trip_list, show_trip


urlpatterns = [
    path("create/", create_trip, name="create_trip"),
    path("trips/", trip_list, name="trip_list"),
    path("trips/<int:trip_id>/", show_trip, name="show_trip"),
]
