# Generated by Django 3.1.1 on 2020-09-22 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aconchego', '0008_room_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='hotel',
        ),
    ]
