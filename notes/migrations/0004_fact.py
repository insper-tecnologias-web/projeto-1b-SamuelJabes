# Generated by Django 4.2.11 on 2024-03-26 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0003_tag_note_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fact",
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
                ("descricao", models.TextField(null=True)),
                ("curtidas", models.IntegerField(default=0)),
            ],
        ),
    ]