from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'venue', 'minimum_amount', 'event_date', 'image']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
        }
        input_formats = ['%d-%m-%Y']
