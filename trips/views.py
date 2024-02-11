from django.shortcuts import render, redirect
from trips.forms import TripForm
from trips.models import Trip
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.author = request.user
            trip.save()
            return redirect('trip_detail', trip_id=trip.id)
    else:
        form = TripForm()
    context = {
        'form': form
    }
    return render(request, "trips/create.html", context)


def trip_list(request):
    trips = Trip.objects.all()
    context = {
        'trips': trips
    }
    return render(request, 'trips/list.html', context)
