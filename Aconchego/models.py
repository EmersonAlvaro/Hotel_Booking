from django.db import models

# Create your models here.

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    localizacao = models.CharField(max_length=255)
    descricao = models.TextField()
    categoria = models.IntegerField(default=0)
    cover = models.ImageField(upload_to='static/img/place/',max_length=255)
    price = models.IntegerField(default=0)
    

# class Room(models.Model):
#     id = models.AutoField(primary_key=True)
#     Numero_cama = models.IntegerField(default=0)
#     tipo = models.CharField(max_length=255)

class Hotel_Fotos(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    path = models.CharField(max_length=255)

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    checkindate = models.DateField(null=True)
    checkoutdate = models.DateField(null=True)
    adultos = models.IntegerField(default=0)
    crianca = models.IntegerField(default=0)
    preco = models.IntegerField(default=0)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=255)
    comment = models.CharField(max_length=255) 