# Generated by Django 4.1.2 on 2022-11-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_movie_category_movie_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year_of_release',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
    ]