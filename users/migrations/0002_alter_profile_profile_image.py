# Generated by Django 4.1.2 on 2022-11-16 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='images/profileImage/user-default.png', upload_to='image/profileImage/'),
        ),
    ]