from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="University",
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
                ("university_rank", models.IntegerField()),
                ("university_name", models.CharField(max_length=30)),
                ("university_country", models.CharField(max_length=30)),
                ("university_global_score", models.IntegerField()),
                ("university_enrollment", models.IntegerField()),
                ("university_link", models.CharField(max_length=100)),
                ("university_photo_link", models.CharField(max_length=100)),
            ],
        ),
    ]
