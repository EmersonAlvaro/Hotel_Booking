import os
import sqlite3
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hotel_Booking.settings")

import django
django.setup()


from Aconchego.models import Room, Hotel, Fotos

hotel = Hotel(
    name="Raphael's Hotel", 
    localizacao='Pemba, Mozambique',
    categoria =3, 
    descricao="o Raphael's Hotel disponibiliza acomodações em Pemba. O hotel dispõe de uma piscina exterior aberta durante todo o ano e de vistas para o mar",
    price = 436, 
    cover = 'img/raphaels/k1.jpg'
)
hotel.save()

room = Room(
    tipo='One-Bedroom Apartment',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=1,
    cover = 'img/raphaels/k2.jpg', 
    price= 130,
) 
room.save()
hotel.rooms.add(room)

room = Room(
    tipo='Superior King Room',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=1,
    cover = 'img/raphaels/k3.jpg', 
    price= 86,
) 
room.save()
hotel.rooms.add(room)

room = Room(
    tipo='Superior King Studio',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=2,
    cover = 'img/raphaels/k4.jpg', 
    price= 86,
) 
room.save()
hotel.rooms.add(room)

room = Room(
    tipo='Superior King Room',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=1,
    cover = 'img/raphaels/k5.jpg', 
    price= 86,
) 
room.save()
hotel.rooms.add(room)

room = Room(
    tipo='Two-Bedroom Apartment',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=2,
    cover = 'img/raphaels/k6.jpg', 
    price= 86,
) 
room.save()
hotel.rooms.add(room)



f5 =Fotos(path='img/raphaels/k7.jpg')
f6 =Fotos(path='img/raphaels/k8.jpg')
f7 =Fotos(path='img/raphaels/k9.jpg')
f8 =Fotos(path='img/raphaels/k10.jpg')


f5.save()
f6.save()
f7.save()
f8.save()

hotel.fotos.add(f5, f6, f7, f8)

hotel.save()


print('Hello There')