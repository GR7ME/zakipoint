# Generated by Django 5.0.6 on 2024-06-04 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endapi', '0003_alter_admins_email_alter_admins_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='email',
            field=models.EmailField(max_length=250),
        ),
        migrations.AlterField(
            model_name='admins',
            name='password',
            field=models.CharField(max_length=250),
        ),
    ]
