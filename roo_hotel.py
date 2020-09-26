import os
import sqlite3
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hotel_Booking.settings")

import django
django.setup()


from Aconchego.models import Room, Hotel, Fotos

hotel = Hotel(
    name="Kaia Village", 
    localizacao='Pemba, Mozambique',
    categoria =3, 
    descricao="Localiza – se na Cidade de Pemba, estrada nº 308, no bairro Mahate",
    price = 436, 
    cover = 'img/kaia/k1.jpg'
)
hotel.save()

room = Room(
    tipo='The Apartments',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=1,
    cover = 'img/kaia/k2.jpg', 
    price= 4000,
) 
room.save()
hotel.rooms.add(room)

room = Room(
    tipo='The Studios',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=1,
    cover = 'img/kaia/k3.jpg', 
    price= 2500,
) 
room.save()
hotel.rooms.add(room)

# f1 =Fotos(path='img/kaia/k3.jpg')
f2 =Fotos(path='img/kaia/k4.jpg')
f3 =Fotos(path='img/kaia/k5.jpg')
f4 =Fotos(path='img/kaia/k6.jpg')
f5 =Fotos(path='img/kaia/k7.jpg')
f6 =Fotos(path='img/kaia/k8.jpg')
f7 =Fotos(path='img/kaia/k9.jpg')
f8 =Fotos(path='img/kaia/k10.jpg')

# f1.save()
f2.save()
f3.save()
f4.save()
f5.save()
f6.save()
f7.save()
f8.save()

hotel.fotos.add(f2, f3, f4, f5, f6, f7, f8)

hotel.save()


print('Hello There======')