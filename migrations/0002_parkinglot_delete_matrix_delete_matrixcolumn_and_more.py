# Generated by Django 4.1.4 on 2023-02-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apms", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ParkingLot",
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
                ("rows", models.PositiveSmallIntegerField()),
                ("columns", models.PositiveSmallIntegerField()),
                ("slots", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="Matrix",
        ),
        migrations.DeleteModel(
            name="MatrixColumn",
        ),
        migrations.DeleteModel(
            name="MatrixRow",
        ),
    ]