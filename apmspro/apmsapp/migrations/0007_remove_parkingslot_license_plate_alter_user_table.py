# Generated by Django 4.1.7 on 2023-02-17 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apmsapp", "0006_parkingslot_license_plate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="parkingslot",
            name="license_plate",
        ),
        migrations.AlterModelTable(
            name="user",
            table=None,
        ),
    ]
