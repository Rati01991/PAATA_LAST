# Generated by Django 4.2.13 on 2024-06-23 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental', '0002_car_image_alter_car_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubmittedCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=8)),
                ('owner_name', models.CharField(max_length=100)),
                ('owner_email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
