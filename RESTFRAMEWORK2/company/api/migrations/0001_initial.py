# Generated by Django 4.2.4 on 2023-09-09 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                (
                    "type",
                    models.CharField(
                        choices=[("IT", "IT"), ("Non-IT", "Non-IT")], max_length=100
                    ),
                ),
                ("added_date", models.DateTimeField(auto_now_add=True)),
                ("active", models.DateField(auto_now=True)),
            ],
        ),
    ]
