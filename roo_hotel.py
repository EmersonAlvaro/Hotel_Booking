import os
import sqlite3
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hotel_Booking.settings")

import django
django.setup()

from Aconchego.models import Room, Hotel, Fotos, Comment

comment = Comment(
    autor='Sam Smith',
    comment='"Working in conjunction with humanitarian aid agencies.'
)
comment.save()

comment = Comment(
    autor='Martin Garrix',
    comment='"Working in conjunction with humanitarian aid agencies.'
)
comment.save()

comment = Comment(
    autor='Erick John',
    comment='"Working in conjunction with humanitarian aid agencies.'
)
comment.save()

comment = Comment(
    autor='Tyler Pose',
    comment='"Working in conjunction with humanitarian aid agencies.'
)
comment.save()

comment = Comment(
    autor='Neymar Jr',
    comment='"Working in conjunction with humanitarian aid agencies.'
)
comment.save()

comment = Comment(
    autor='Leo Messi',
    comment='"Working in conjunction with humanitarian aid agencies.'
)
comment.save()

comment = Comment(
    autor='Luis Suares',
    comment='"Working in conjunction with humanitarian aid agencies.'
)
comment.save()

comment = Comment(
    autor='David Ant',
    comment='"Working in conjunction with humanitarian aid agencies.'
)
comment.save()


print('Hello There')


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

