# Generated by Django 3.1.1 on 2020-09-21 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aconchego', '0004_auto_20200921_1125'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='Room_Fotos',
        ),
        migrations.AddField(
            model_name='hotel_fotos',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Aconchego.hotel'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Aconchego.hotel'),
        ),
        migrations.AlterField(
            model_name='hotel_fotos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
