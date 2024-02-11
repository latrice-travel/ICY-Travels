from django.shortcuts import render, redirect, get_object_or_404
from trips.forms import TripForm
from trips.models import Trip
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def create_trip(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("trip_list")

    else:
        form = TripForm()
    context = {"form": form}
    return render(request, "trips/create.html", context)


def show_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    context = {
        "trip": trip,
    }
    return render(request, "trips/detail.html", context)


def trip_list(request):
    trips = Trip.objects.all()
    context = {"trips": trips}
    return render(request, "trips/list.html", context)
