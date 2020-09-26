from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *
from .forms import *
import random 

# Create your views here.

def aconchego(request):

    hoteis = Hotel.objects.all().order_by('?')
    comments = Comment.objects.all().order_by('?')
    searchform = SearchForm()

    context = {
        'hoteis': hoteis[:6],
        'comments': comments[:5],
        'searchform': searchform, 
    }
    return render(request, 'index.html', context=context)


def hotels(request):

    hoteis = Hotel.objects.all()
    searchform = SearchForm()
    filterform = FilterForm()

    context = {
        'hoteis': hoteis,
        'searchform': searchform,
        'filterform': filterform,
    }
    
    return render(request, 'hotels.html', context=context)


    
def hotel_details(request, pk):

    hotel = Hotel.objects.get(pk=pk)

    if request.method == 'POST':
        print("Hello There")
        forma = ReservaForm(request.POST)
        if forma.is_valid():
            # forma.save()
            obj = forma.save(commit=False)
            obj.hotel = hotel
            obj.price =obj.room.price
            obj.save()
            return redirect ('reserva', pk=obj.pk)
        
    else:
        
        hotel_fotos = hotel.fotos.all()
        rooms = hotel.rooms.all()
        form = ReservaForm(initial={'room':rooms, })

        context = {
            'hotel': hotel,
            'form': form,
            'hotel_fotos': hotel_fotos,
            'rooms': rooms,
        }    
        
    return render(request, 'hotel_details.html', context=context)


def reserva(request, pk):

    if request.method == 'POST':
        print("Hello There")
        fullform = FullReservaForm(request.POST)
        if fullform.is_valid():
            
            obj = fullform.save(commit=False)

            customer = Customer()
            customer.first_name = fullform.cleaned_data.get('first_name')
            customer.last_name = fullform.cleaned_data.get('last_name')
            customer.email_address = fullform.cleaned_data.get('email')
            
            obj.customer = customer
            
            customer.save()
            obj.save()

            return redirect ('hotel_details', pk=obj.hotel.pk)

    else:    

        rese = Reserva.objects.get(pk=pk)
        
        fullform = FullReservaForm(
            initial={
                'adultos': rese.adultos,
                'crianca': rese.crianca,
                'checkindate':rese.checkindate,
                'checkoutdate':rese.checkoutdate,
                'room': rese.room,
                'hotel':rese.hotel,
                'preco': rese.preco,
            }
        )
    
        context = {'fullform':fullform,}
    
    return render(request, 'reserva.html', context=context)

def contacto(request):
    context = {}
    return render(request, 'contacto.html', context=context)

def about(request):
    context = {}
    return render(request, 'about.html', context=context)
