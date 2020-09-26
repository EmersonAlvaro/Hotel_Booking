import os
import sqlite3
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hotel_Booking.settings")

import django
django.setup()


from Aconchego.models import Room, Hotel, Fotos

hotel = Hotel(
    name="The Nautilus ", 
    localizacao='Pemba, Mozambique',
    categoria =3, 
    descricao="o TheNautilus Pemba está situado na cidade de Pemba. Os hóspedes podem desfrutar do restaurante,é um local extremamente aconchegante e óptimo atendimento.",
    price = 436, 
    cover = 'img/nautilus/k1.jpg'
)
hotel.save()

room = Room(
    tipo='Standard Room',
    descricao='Quarto de hotel composto por cama Queen size ou duas camas single, varanda com vistas para o jardim e mar.', 
    Numero_cama=1,
    cover = 'img/nautilus/k2.jpg', 
    price= 13768,
) 
room.save()
hotel.rooms.add(room)



f1 =Fotos(path='img/nautilus/k3.jpg')
f2 =Fotos(path='img/nautilus/k4.jpg')
f3 =Fotos(path='img/nautilus/k5.jpg')
f4 =Fotos(path='img/nautilus/k6.jpg')
f5 =Fotos(path='img/nautilus/k7.jpg')
f6 =Fotos(path='img/nautilus/k8.jpg')
f7 =Fotos(path='img/nautilus/k9.jpg')
f8 =Fotos(path='img/nautilus/k10.jpg')

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