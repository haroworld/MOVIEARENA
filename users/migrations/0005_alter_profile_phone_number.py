# Generated by Django 4.1.2 on 2022-12-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_phone_number_profile_profiles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]
