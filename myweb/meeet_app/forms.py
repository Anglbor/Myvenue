from django import forms
from django.forms import ModelForm
from .models import Meet, Venue, MyUsers

class MeetForm(ModelForm):
    class Meta:
        model = Meet
        # fields = '__all__'
        fields = ('name', 'meet_date', 'venue', 'manager', 'guests', 'description', )

        labels = {
            'name': '',
            'meet_date': '',
            'venue': 'Venue',
            'manager': 'Manager',
            'guests': 'Guests',
            'description': '',

        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meeting name'}),
            'meet_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meeting date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Manager'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'guests': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Guests'}),

        }

# creating venue forms
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        # fields = '__all__'
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email')

        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email': '',

        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip-code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Webside'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),

        }