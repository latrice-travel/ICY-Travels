from django import forms
from trips.models import Trip

class TripForm(forms.ModelForm):
    TRIP_CHOICES = [
        ('future', 'Future Trip'),
        ('past', 'Past Trip')
    ]

    trip_type = forms.ChoiceField(
        label='Trip Type',
        choices=TRIP_CHOICES,
        widget=forms.RadioSelect,
        initial='future',
    )

    class Meta:
        model = Trip
        fields = [
            'title',
            'picture',
            'description',
            'location',
        ]
