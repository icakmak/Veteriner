# Generated by Django 3.2.9 on 2021-11-10 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=120)),
                ('c_photo', models.CharField(max_length=120)),
                ('c_address', models.CharField(max_length=250)),
                ('c_city', models.CharField(max_length=120)),
                ('c_phone', models.CharField(max_length=20)),
                ('c_created_at', models.DateTimeField(auto_now_add=True)),
                ('c_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kindName', models.CharField(max_length=50)),
                ('c_created_at', models.DateTimeField(auto_now_add=True)),
                ('c_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=120)),
                ('a_photo', models.CharField(max_length=120)),
                ('a_birthdate', models.DateField()),
                ('a_created_at', models.DateTimeField(auto_now_add=True)),
                ('a_updated_at', models.DateTimeField(auto_now=True)),
                ('a_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sahipler', to='VetApps.customer')),
                ('a_kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turler', to='VetApps.kind')),
            ],
        ),
    ]
