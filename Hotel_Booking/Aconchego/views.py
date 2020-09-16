from django.shortcuts import render

# Create your views here.

def aconchego(request):
    context={}
    return render(request, 'index.html', context=context)

def hotels(request):
    context={}
    return render(request, 'hotels.html', context=context)

def about(request):
    context={}
    return render(request, 'about.html', context=context)

def contacto(request):
    context={}
    return render(request, 'contacto.html', context=context)


