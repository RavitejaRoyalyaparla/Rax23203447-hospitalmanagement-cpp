# Generated by Django 5.0.4 on 2024-04-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]