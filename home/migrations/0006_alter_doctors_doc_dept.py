# Generated by Django 5.0.4 on 2024-04-22 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doc_dept',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.departments'),
        ),
    ]
