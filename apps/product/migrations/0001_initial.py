# Generated by Django 4.2.2 on 2023-07-25 07:42

import apps.product.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vendor", "0003_vendor_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200)),
                ("ordering", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ["ordering"],
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=150)),
                ("slug", models.SlugField(max_length=150)),
                ("price", models.IntegerField()),
                ("small_description", models.TextField(max_length=150)),
                ("description", models.TextField()),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "image",
                    models.ImageField(upload_to=apps.product.models.get_file_path),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="product.category",
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="vendor.vendor",
                    ),
                ),
            ],
        ),
    ]
