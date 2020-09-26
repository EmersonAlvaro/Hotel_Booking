import os
import sqlite3
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hotel_Booking.settings")

import django
django.setup()


from Aconchego.models import Room, Hotel, Fotos

hotel = Hotel(
    name="Kirimizi Hotel", 
    localizacao='Pemba, Mozambique',
    categoria =4, 
    descricao="Kirimizi Hotel & Restaurante disponibiliza acomodações com um restaurante, estacionamento privado gratuito, uma piscina exterior e um bar.  Quarto espaçoso e confortável , com vista maravilhosa da praia, do recanto da piscina.",
    price = 436, 
    cover = 'img/kirimizi/k1.jpg'
)
hotel.save()

room = Room(
    tipo='Quarto Standard',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=1,
    cover = 'img/kirimizi/k2.jpg', 
    price= 9230,
) 
room.save()
hotel.rooms.add(room)


f1 =Fotos(path='img/kirimizi/k3.jpg')
f2 =Fotos(path='img/kirimizi/k4.jpg')
f3 =Fotos(path='img/kirimizi/k5.jpg')
f4 =Fotos(path='img/kirimizi/k6.jpg')
f5 =Fotos(path='img/kirimizi/k7.jpg')
f6 =Fotos(path='img/kirimizi/k8.jpg')
f7 =Fotos(path='img/kirimizi/k9.jpg')
f8 =Fotos(path='img/kirimizi/k10.jpg')

f1.save()
f2.save()
f3.save()
f4.save()
f5.save()
f6.save()
f7.save()
f8.save()

hotel.fotos.add(f1, f2, f3, f4, f5, f6, f7, f8)

hotel.save()


print('Hello There')