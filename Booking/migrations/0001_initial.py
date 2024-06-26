# Generated by Django 5.0.6 on 2024-05-27 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0001_initial'),
        ('Hotel', '0001_initial'),
        ('Room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_time', models.DateTimeField(max_length=255, null=True)),
                ('check_out_time', models.DateTimeField(max_length=255, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.guest')),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel.hotel')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.room')),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
