from django import forms 
from .models import Reserva

class DateInput(forms.DateInput):
    input_type='date'

class ReservaForm(forms.ModelForm):

    checkindate = forms.DateTimeField(widget=DateInput(attrs={'class': 'form-control'}))
    checkoutdate = forms.DateTimeField(widget=DateInput(attrs={'class': 'form-control'}))
    # adultos = forms.IntegerField

    class Meta:
        model = Reserva
        fields = [
            'checkindate',
            'checkoutdate', 
            'adultos',
            'crianca', 
        ]
        widgets = {
            'adultos': forms.TextInput(attrs={'class': 'form-control', 'type':"number"}),
            'crianca': forms.TextInput(attrs={'class': 'form-control', 'type':"number", 'placeholder':"Check In Date" }),
            
            'checkindate': forms.DateInput(attrs={'class': 'form-control'}),
        }
