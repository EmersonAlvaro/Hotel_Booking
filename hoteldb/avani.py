import os
import sqlite3
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hotel_Booking.settings")

import django
django.setup()


from Aconchego.models import Room, Hotel, Fotos

hotel = Hotel(
    name="Avani Pemba Beach", 
    localizacao='Pemba, Mozambique',
    categoria =5, 
    descricao="o Avani Pemba Beach hotel, está localizado entre a Baía de Pemba e a Praia Wimbe. Espaço com quartos espaçosos e confortáveis, entretenimento, comida típica e estrangeira",
    price = 4363, 
    cover = 'img/avani/k1.jpg'
)
hotel.save()

room = Room(
    tipo='Avani Room',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=1,
    cover = 'img/avani/k2.jpg', 
    price= 13768,
) 
room.save()
hotel.rooms.add(room)

room = Room(
    tipo='Avani Garden Room',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=1,
    cover = 'img/avani/k3.jpg', 
    price= 18768,
) 
room.save()
hotel.rooms.add(room)

room = Room(
    tipo='Avani Ocean Room',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=1,
    cover = 'img/avani/k4.jpg', 
    price= 19768,
) 
room.save()
hotel.rooms.add(room)

room = Room(
    tipo='Avani Ocean Deluxe Suite',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=1,
    cover = 'img/avani/k5.jpg', 
    price= 19768,
) 
room.save()
hotel.rooms.add(room)


room = Room(
    tipo='Avani One Bedroom Garden Apartament',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=1,
    cover = 'img/avani/k6.jpg', 
    price= 23456,
) 
room.save()
hotel.rooms.add(room)

f1 =Fotos(path='img/avani/k11.jpg')
f5 =Fotos(path='img/avani/k7.jpg')
f6 =Fotos(path='img/avani/k8.jpg')
f7 =Fotos(path='img/avani/k9.jpg')
f8 =Fotos(path='img/avani/k10.jpg')

f1.save()
f5.save()
f6.save()
f7.save()
f8.save()

hotel.fotos.add(f1, f5, f6, f7, f8)

hotel.save()


print('Hello There')