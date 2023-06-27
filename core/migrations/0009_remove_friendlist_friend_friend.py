# Generated by Django 4.1.7 on 2023-06-15 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0008_alter_friendlist_friend"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="friendlist",
            name="friend",
        ),
        migrations.CreateModel(
            name="Friend",
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
                (
                    "friend",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "friendlist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.friendlist",
                    ),
                ),
            ],
        ),
    ]
