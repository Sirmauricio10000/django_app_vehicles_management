# Generated by Django 3.2.9 on 2024-10-25 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transportation_management', '0002_rename_route_vehicle_route_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='route_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transportation_management.route'),
        ),
    ]
