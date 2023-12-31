# Generated by Django 4.2.4 on 2023-09-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("emp_name", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("companyName", models.CharField(max_length=100)),
                ("salary", models.IntegerField()),
            ],
        ),
    ]
