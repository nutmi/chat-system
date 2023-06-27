# Generated by Django 4.1.7 on 2023-06-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_message_room"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="room",
        ),
        migrations.AddField(
            model_name="message",
            name="text",
            field=models.TextField(null=True),
        ),
    ]