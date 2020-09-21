from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .forms import ReservaForm
import random

 

# Create your views here.


def aconchego(request):

    hoteis = Hotel.objects.all().order_by('?')
    comments = Comment.objects.all().order_by('?')

    context = {
        'hoteis': hoteis[:6],
        'comments': comments[:5]
    }
    return render(request, 'index.html', context=context)


def hotels(request):

    hoteis = Hotel.objects.all()

    context = {
        'hoteis': hoteis[:6],
    }
    return render(request, 'hotels.html', context=context)


def hotels_details(request, pk):

    hotel = Hotel.objects.get(pk=pk)
    hotel_fotos = Hotel_Fotos.objects.filter(hotel=pk)
    form = ReservaForm()

    context = {
        'hotel': hotel,
        'form': form,
        'hotel_fotos': hotel_fotos,
    }

    if request.method == 'POST':
        # print("Hello There")
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            print("Hello There")

    return render(request, 'hotel_details.html', context=context)


def about(request):
    context = {}
    return render(request, 'about.html', context=context)


def contacto(request):
    context = {}
    return render(request, 'contacto.html', context=context)
