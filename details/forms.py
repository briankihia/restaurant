# forms.py

from django import forms
from .models import DailyDuty,Reservation


# Create a Django form that allows the superuser to set duties for each employee on a given day.

# class DutyForm(forms.ModelForm):
#     class Meta:
#         model = DailyDuty
#         fields = ['day', 'employee', 'duty']


# FORMS.PY IS USED WHEN YOU WANT TO USE BUILT-IN FORMS OF DJANGO

# forms.py


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'reservation_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial queryset for reservation_date
        self.fields['reservation_date'].queryset = Reservation.objects.values_list('available_dates', flat=True)

        # Add the "datepicker" class to the widget for styling
        self.fields['reservation_date'].widget.attrs['class'] = 'datepicker'
