# Generated by Django 3.1.1 on 2020-09-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aconchego', '0004_delete_room_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='rooms',
            field=models.ManyToManyField(to='Aconchego.Room'),
        ),
    ]
