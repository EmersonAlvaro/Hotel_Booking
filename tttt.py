import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hotel_Booking.settings")

import django
django.setup()

from Aconchego.models import Hotel, Comment

# hotel = Hotel(
#     name="Wimbi Sun", 
#     localizacao='Pemba, Mozambique',
#     categoria =3, 
#     descricao="HHoaonjffnjfnjfndjnfjnvdfjdfjndfjv",
#     price = 436, 
#     cover = 'img/place/5.png'
# )

# hotel.save()
comment = Comment(
    autor='Sam Smith',
    comment='"Working in conjunction with humanitarian aid agencies.'
)
comment.save()
print('Hello There')