# Generated by Django 4.2 on 2023-04-23 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=200)),
                ('home_adress', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='HomeAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ_pojisteni', models.CharField(max_length=80)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epojapp.client')),
            ],
        ),
    ]