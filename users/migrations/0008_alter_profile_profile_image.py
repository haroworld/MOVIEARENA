# Generated by Django 4.1.2 on 2022-12-28 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='images/profileImage/user-default.png', upload_to='images/profileImage/'),
        ),
    ]
