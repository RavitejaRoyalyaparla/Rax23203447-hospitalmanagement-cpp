# Generated by Django 5.0.4 on 2024-04-11 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_departments_dept_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=50)),
                ('doc_spec', models.CharField(max_length=100)),
                ('doc_image', models.ImageField(upload_to='doctors')),
                ('doc_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.departments')),
            ],
        ),
    ]
