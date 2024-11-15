# Generated by Django 5.0.6 on 2024-08-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('password', models.CharField(max_length=128)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='other', max_length=100)),
                ('birthdate', models.DateTimeField()),
                ('created_by', models.DateTimeField(auto_now=True)),
                ('updated_by', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
