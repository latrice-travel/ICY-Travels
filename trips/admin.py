from django.contrib import admin
from trips.models import Trip
# Register your models here.


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'picture',
        'description',
        'location',
        'author',
        'created_at',
        'past_trip',
        'future_trip',

    )
