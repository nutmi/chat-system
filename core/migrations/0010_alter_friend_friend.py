# Generated by Django 4.1.7 on 2023-06-15 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0009_remove_friendlist_friend_friend"),
    ]

    operations = [
        migrations.AlterField(
            model_name="friend",
            name="friend",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
