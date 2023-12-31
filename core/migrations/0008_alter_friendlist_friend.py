# Generated by Django 4.1.7 on 2023-06-14 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0007_friendlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="friendlist",
            name="friend",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="friend",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
