# Generated by Django 5.1.2 on 2024-11-04 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_personal', models.CharField(max_length=50, unique=True)),
                ('clave_personal', models.CharField(max_length=50)),
                ('nombre_personal', models.CharField(max_length=100)),
            ],
        ),
    ]
