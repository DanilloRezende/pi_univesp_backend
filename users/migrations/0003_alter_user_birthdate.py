# Generated by Django 5.0.6 on 2024-09-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
