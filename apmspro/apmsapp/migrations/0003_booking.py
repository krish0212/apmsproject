# Generated by Django 4.1.7 on 2023-02-16 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("apmsapp", "0002_alter_parkingslot_slots"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                (
                    "parking_slot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apmsapp.parkingslot",
                    ),
                ),
            ],
        ),
    ]
