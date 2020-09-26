import os
import sqlite3
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hotel_Booking.settings")

import django
django.setup()

# cc = sqlite3.connect("db.sqlite3")
# cc.execute("INSERT INTO Aconchego_hotel_fotos VALUES ('img/elements/g11.jpg', 1, 98);")

from Aconchego.models import Hotel, Comment, Hotel_Fotos


# hotel = Hotel(
#     name="Chuiba Baylodge", 
#     localizacao='Pemba, Mozambique',
#     categoria =3, 
#     descricao="O ChuibaBayLodge está situado nas dunas ao longo da Praia de Chuiba, apenas a 9 km de Pemba. Dispõe de uma piscina exterior, de um restaurante e de um bar, quartos super confortáveis e espaços",
#     price = 436, 
#     cover = 'img/place/5.png'
# )
# hotel.save()

# hotel = Hotel(
#     name="Guest house Samotina", 
#     localizacao='Pemba, Mozambique',
#     categoria =3, 
#     descricao="Situado em Pemba, a 1.5 km do Centro Comercial Pemba e a 3,2 km da KaskaziniTravel, o GuesthouseSamotina disponibiliza acomodações com acesso Wi-Fi gratuito, ar condicionado, um bar e um jardim",
#     price = 436, 
#     cover = 'img/place/1.png'
# )
# hotel.save()

# hotel = Hotel(
#     name="Situ Island", 
#     localizacao='Pemba, Mozambique',
#     categoria =3, 
#     descricao="Com uma área de praia privada e oportunidades de mergulho, a remota Situ Island situa-se no Arquipélago das Quirimbas e Pemba é a cidade mais próxima. Ailhaapenas é acessível porvia maritima",
#     price = 436, 
#     cover = 'img/place/3.png'
# )
# hotel.save()

# hotel = Hotel(
#     name="UlalaLodge Murrébuè", 
#     localizacao='Pemba, Mozambique',
#     categoria =3, 
#     descricao="O UlalaLodge goza de uma localização tranquila na Praia de Murrébué, a 15 minutos da Cidade de Pemba. Este alojamento ecológico e isolado alberga um acolhedor restaurante e bar enfrente a  praia",
#     price = 436, 
#     cover = 'img/place/5.png'
# )
# hotel.save()

# hotel = Hotel(
#     name="Aparthotel Mozambique-Pemba", 
#     localizacao='Pemba, Mozambique',
#     categoria =3, 
#     descricao="Localizado na cidade de Pemba, na estrada nº 125 Praia do Wimbe, Bairro Nanhimbe, Pemba Moçambique, o Apart Hotel contem um conjunto de quartos confortaveis e muito acessivel ao bolso de qualquer um dos clientes",
#     price = 436, 
#     cover = 'img/place/5.png'
# )
# hotel.save()

# hotel = Hotel(
#     name="Complexo Turístico Caracol", 
#     localizacao='Pemba, Mozambique',
#     categoria =3, 
#     descricao="Localizada na praia do Wimbi, um conjunto de quartos confortáveis e muito acessível ao bolso de qualquer um dos clientes, oferecemos acesso a rede de internet gratuito e pequeno-almoço",
#     price = 436, 
#     cover = 'img/place/4.png'
# )
# hotel.save()

# hotel = Hotel(
#     name="Hotel Sarima", 
#     localizacao='Pemba, Mozambique',
#     categoria =3, 
#     descricao="Localiza-se na avenida marginal praia do wimbi, com acesso a rede de internet super grátis e uma bela vista para a praia de wimbi",
#     price = 436, 
#     cover = 'img/place/5.png'
# )
# hotel.save()





# hotel = Hotel(
#     name="Meg-Residencial", 
#     localizacao='Pemba, Mozambique',
#     categoria =3, 
#     descricao="Localiza-se na avenida 25 de Setembro nas instalações da Universidade Católica de Moçambique, delegação de Pemba.",
#     price = 436, 
#     cover = 'img/place/5.png'
# )
# hotel.save()

# hotel = Hotel(
#     name="Residencial ReggioEmilia", 
#     localizacao='Pemba, Mozambique',
#     categoria =3, 
#     descricao="Localizada na cidade de Pemba, na Avenida Marginal, Numero 8696, Praia do Wimbi.",
#     price = 436, 
#     cover = 'img/place/5.png'
# )
# hotel.save()

