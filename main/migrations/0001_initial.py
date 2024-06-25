# Generated by Django 5.0.1 on 2024-06-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
    ]
