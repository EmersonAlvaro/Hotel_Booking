from django import forms
from .models import *


class ReservaForm(forms.ModelForm):

    def __init__(self, hotel, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)
        self.fields['room'] =forms.ModelChoiceField(queryset=hotel.rooms.all())

    class Meta:
        model = Reserva

        fields = [
                'checkindate',
                'checkoutdate', 
                'adultos',
                'crianca', 
                'room',
        ]

class CustomerForm (forms.ModelForm):

    class Meta:
        model = Customer

        fields = [
            'last_name',
            'first_name',
            'email_address',
        ]

class FullReservaForm(forms.ModelForm):
    last_name = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255) 

    class Meta:
        model = Reserva

        fields = [
                'checkindate',
                'checkoutdate', 
                'adultos',
                'crianca', 
                'room',
                'hotel',
                'preco',
                'last_name',
                'first_name',
                'email'
        ]

class SearchForm(forms.Form):

    checkindate = forms.DateField()
    checkoutdate = forms.DateField()
    adultos = forms.IntegerField()
    crianca = forms.IntegerField()

    fields = [
                'checkindate',
                'checkoutdate', 
                'adultos',
                'crianca', 
    ]

class FilterForm(forms.Form):

    CATEGORIAS_CHOICES = (
        ("0", "Choose Here"),
        ("1", "One Star"),
        ("2", "Two Star"),
        ("3", "Three Star"),
        ("4", "Four Star"),
        ("5", "Five Star"),
    )

    categoria = forms.ChoiceField(choices=CATEGORIAS_CHOICES)
    price = forms.CharField(max_length=255)

    fields = [
                'categoria',
                'price',
            ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

    fields = [
                'username',
                'password', 
    ]

