# Generated by Django 5.0.6 on 2024-05-27 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel.hotel')),
            ],
            options={
                'db_table': 'menu',
            },
        ),
    ]
