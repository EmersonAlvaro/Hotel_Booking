from django.db import models

# Create your models here.

class Room(models.Model):
    # id = models.AutoField(primary_key=True)
    Numero_cama = models.IntegerField(default=0)
    tipo = models.CharField(max_length=255)
    descricao = models.TextField(null=True)
    cover = models.ImageField(upload_to='static/img/place/',max_length=255, null=True)
    price = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.tipo)

class Customer (models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)

class Fotos(models.Model):
    # id = models.AutoField(primary_key=True)
    path = models.ImageField(upload_to='static/img/place/',max_length=255)

class Hotel(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    localizacao = models.CharField(max_length=255)
    descricao = models.TextField()
    categoria = models.IntegerField(default=0)
    cover = models.ImageField(upload_to='static/img/place/',max_length=255)
    price = models.IntegerField(default=0)
    rooms = models.ManyToManyField(Room)
    fotos = models.ManyToManyField(Fotos)

    def __str__(self):
        return str(self.name)

class Reserva(models.Model):
    # id = models.AutoField(primary_key=True)
    checkindate = models.DateField(null=True)
    checkoutdate = models.DateField(null=True)
    adultos = models.IntegerField(default=0)
    crianca = models.IntegerField(default=0)
    preco = models.IntegerField(default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    # id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)