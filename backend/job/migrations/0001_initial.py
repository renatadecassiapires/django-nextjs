# Generated by Django 4.2.2 on 2023-06-28 20:01

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(max_length=200, null=True)),
                ("description", models.TextField(null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("address", models.CharField(max_length=100, null=True)),
                (
                    "jobType",
                    models.CharField(
                        choices=[
                            ("Permanent", "Permanent"),
                            ("Temporary", "Temporary"),
                            ("Intership", "Intership"),
                        ],
                        default="Permanent",
                        max_length=10,
                    ),
                ),
                (
                    "Education",
                    models.CharField(
                        choices=[
                            ("Bachelors", "Bachelors"),
                            ("Masters", "Masters"),
                            ("Phd", "Phd"),
                        ],
                        default="Bachelors",
                        max_length=10,
                    ),
                ),
                (
                    "Industry",
                    models.CharField(
                        choices=[
                            ("Business", "Business"),
                            ("Information Technology", "It"),
                            ("Banking", "Banking"),
                            ("Education/Training", "Education"),
                            ("Telecomunication", "Telecomunication"),
                            ("Others", "Others"),
                        ],
                        default="Business",
                        max_length=30,
                    ),
                ),
                (
                    "Experiency",
                    models.CharField(
                        choices=[
                            ("No Experience", "No Experience"),
                            ("1 Years", "One Year"),
                            ("2 Years", "Two Years"),
                            ("3 Years above", "Three Years Plus"),
                        ],
                        default="No Experience",
                        max_length=20,
                    ),
                ),
                (
                    "salary",
                    models.IntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(1000000),
                        ],
                    ),
                ),
                ("positions", models.IntegerField(default=1)),
                ("company", models.CharField(max_length=100, null=True)),
                (
                    "point",
                    django.contrib.gis.db.models.fields.PointField(
                        default=django.contrib.gis.geos.point.Point(0.0, 0.0), srid=4326
                    ),
                ),
                ("lastDate", models.DateTimeField(default=job.models.return_date_time)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
