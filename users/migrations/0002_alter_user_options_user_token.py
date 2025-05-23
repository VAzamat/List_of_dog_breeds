# Generated by Django 4.2.13 on 2025-04-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="token",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="проверочный код для подтверждения пользователя",
            ),
        ),
    ]
