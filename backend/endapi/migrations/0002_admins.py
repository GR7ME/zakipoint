# Generated by Django 5.0.6 on 2024-06-04 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]