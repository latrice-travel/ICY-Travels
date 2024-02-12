from django.shortcuts import render, redirect, get_object_or_404
from trips.forms import TripForm
from trips.models import Trip
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
    login_url = reverse("login")
    signup_url = reverse("signup")
    context = {
        "trips": trips,
        "login_url": login_url,
        "signup_url": signup_url,
    }
    return render(request, "trips/list.html", context)

@login_required
def edit_trip(request, id):
    trip = get_object_or_404(Trip, id=id)
    if request.method == "POST":
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect("show_trip", id=id)
    else:
        form = TripForm(instance=trip)
    context = {
        "form": form,
        "trip": trip,
    }
    return render(request, "trips/edit.html", context)


@login_required
def delete_trip(request, id):
    trip = get_object_or_404(Trip, id=id)
    if request.method == "POST":
        trip.delete()
        return redirect("trip_list")
    context = {"trip": trip}
    return render(request, "trips/delete.html", context)
