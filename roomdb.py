import os
import sqlite3
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hotel_Booking.settings")

import django
django.setup()


from Aconchego.models import Room

room = Room(
    tipo='Quarto solteiro',
    descricao='Quarto de hotel para uma pessoa, com uma cama de solteiro', 
    Numero_cama=1,
    cover = 'img/elements/g1.jpg'
)
room.save()

room = Room(
    tipo='Quarto duplo solteiro',
    descricao='Quarto de hotel com duas camas de solteiro destinadas a duas pessoas. ', 
    Numero_cama=2,
    cover = 'img/elements/g1.jpg'
)
room.save()

room = Room(
    tipo='Quarto casal',
    descricao='Quarto de hotel destinado a duas pessoas,com uma cama de casal.', 
    Numero_cama=1,
    cover = 'img/elements/g1.jpg'
)
room.save()

room = Room(
    tipo='Quartos dormitórios',
    descricao='Quarto de hotel com várias camas, incluindo beliches e,  triliches', 
    Numero_cama=5,
    cover = 'img/elements/g1.jpg'
)
room.save()

room = Room(
    tipo='Quarto Standard',
    descricao='Quarto de hotel que conta com os serviços mais básicos para seus hóspedes.', 
    Numero_cama=1,
    cover = 'img/elements/g1.jpg'
)
room.save()

room = Room(
    tipo='Quarto Master',
    descricao='Quarto de hotel chamados de executivos, são maiores, com boa vista e localização', 
    Numero_cama=1,
    cover = 'img/elements/g1.jpg'
)
room.save()

room = Room(
    tipo='Quarto Deluxe',
    descricao='Quarto de hotel que conta com portas que separam ambientes,com banheiras e a melhor vista do hotel', 
    Numero_cama=1,
    cover = 'img/elements/g1.jpg'
)
room.save()



print('Hello There')