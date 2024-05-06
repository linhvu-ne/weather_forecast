# Generated by Django 5.0.4 on 2024-05-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Weather",
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
                ("city", models.CharField(max_length=100)),
                ("country_code", models.CharField(max_length=50)),
                ("lon", models.DecimalField(decimal_places=4, max_digits=7)),
                ("lat", models.DecimalField(decimal_places=2, max_digits=4)),
                ("pressure", models.IntegerField()),
                ("humidity", models.IntegerField()),
                ("updated_time", models.DateTimeField(auto_now=True)),
                ("tempC", models.FloatField()),
            ],
        ),
    ]