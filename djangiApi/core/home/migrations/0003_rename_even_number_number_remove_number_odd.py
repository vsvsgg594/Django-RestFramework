# Generated by Django 4.2.4 on 2023-08-19 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_number"),
    ]

    operations = [
        migrations.RenameField(
            model_name="number", old_name="even", new_name="number",
        ),
        migrations.RemoveField(model_name="number", name="odd",),
    ]
