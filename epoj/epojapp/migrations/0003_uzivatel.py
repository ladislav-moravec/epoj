# Generated by Django 4.2 on 2023-04-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epojapp', '0002_insurancetype_remove_client_home_adress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uzivatel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'uživatel',
                'verbose_name_plural': 'uživatelé',
            },
        ),
    ]