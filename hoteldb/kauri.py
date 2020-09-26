import os
import sqlite3
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hotel_Booking.settings")

import django
django.setup()


from Aconchego.models import Room, Hotel, Fotos

hotel = Hotel(
    name="Kauri Resort", 
    localizacao='Pemba, Mozambique',
    categoria =3, 
    descricao="Situada na cidade de Pemba, em plena Avenida da Marginal Bairro Nanhimbe, Pemba numero 20201. O Kauri Resort, oferece uma bela e óptima vista de uma das mas belas praias da capital de Cabo Delgado",
    price = 436, 
    cover = 'img/kauri/k2.jpg'
)
hotel.save()

room = Room(
    tipo='Quarto solteiro standard',
    descricao='Quarto de hotel para uma pessoa, com uma cama de solteirocom área de 24 m2.', 
    Numero_cama=1,
    cover = 'img/kauri/k10.jpg', 
    price= 5500,
) 
room.save()
hotel.rooms.add(room)

room = Room(
    tipo='Suite Executiva',
    descricao='Quarto de hotel com duas camas de solteiro destinadas a duas pessoas, com área de 70 m2. ', 
    Numero_cama=2,
    cover = 'img/kauri/k13.jpg',
    price= 12500,
)
room.save()
hotel.rooms.add(room)

room = Room(
    tipo='Quarto casal',
    descricao='Quarto de hotel destinado a duas pessoas,com uma cama de casal.', 
    Numero_cama=1,
    cover = 'img/kauri/k8.jpg', 
    price= 7500,
)
room.save()
hotel.rooms.add(room)

room = Room(
    tipo='Quarto casal ou duplo standard',
    descricao='Quarto de hotel destinado a duas pessoas,com uma cama de casal.', 
    Numero_cama=2,
    cover = 'img/kauri/k12.jpg', 
    price= 6500,
)
room.save()
hotel.rooms.add(room)

room = Room(
    tipo='Quarto familiar',
    descricao='Quarto de hotel destinado a duas pessoas,com uma cama de casal.', 
    Numero_cama=1,
    cover = 'img/kauri/k12.jpg', 
    price= 7000,
)
room.save()
hotel.rooms.add(room)


f1 =Fotos(path='img/kauri/k1.jpg')
f2 =Fotos(path='img/kauri/k4.jpg')
f3 =Fotos(path='img/kauri/k5.jpg')
f4 =Fotos(path='img/kauri/k6.jpg')
f5 =Fotos(path='img/kauri/k7.jpg')
f6 =Fotos(path='img/kauri/k9.jpg')

f1.save()
f2.save()
f3.save()
f4.save()
f5.save()
f6.save()


hotel.fotos.add(f1, f2, f3, f4, f5, f6)

hotel.save()


print('Hello There')