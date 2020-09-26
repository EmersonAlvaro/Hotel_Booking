import os
import sqlite3
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hotel_Booking.settings")

import django
django.setup()

# cc = sqlite3.connect("db.sqlite3")
# cc.execute("INSERT INTO Aconchego_hotel_fotos VALUES ('img/elements/g11.jpg', 1, 98);")

from Aconchego.models import *
hotel = Hotel.objects.get(id=15)

fotos1 = Fotos.objects.get(id=1)
fotos2 = Fotos.objects.get(id=2)
fotos3 = Fotos.objects.get(id=3)
fotos4 = Fotos.objects.get(id=4)
fotos5 = Fotos.objects.get(id=5)
fotos6 = Fotos.objects.get(id=6)
fotos7 = Fotos.objects.get(id=7)
fotos8 = Fotos.objects.get(id=8)

hotel.fotos.add(
    fotos1,fotos2, fotos3, fotos4, fotos5, fotos6, fotos7, fotos8
)
hotel.save()

print('Hello There')