# Generated by Django 4.1.2 on 2022-11-25 10:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_movie_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('movie_category', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.categories'),
        ),
    ]
