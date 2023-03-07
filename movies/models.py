from django.db import models
import uuid
# Create your models here.


class Categories(models.Model):
    movie_category = models.CharField(max_length=200)
    movies = models.ManyToManyField("movie", null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.movie_category


class movie(models.Model):
    RATING = (
        ('18','18'),
        ('R','R'),
        ('PG-13','PG-13'),
        ('PG','PG'),
        ('G','G'),
    )

    year_of_release = models.CharField(max_length=50)
    category = models.ManyToManyField(Categories)
    main_category = models.ForeignKey("Categories", related_name="main_category", on_delete=models.SET_NULL,null=True)
    movie_name = models.CharField(max_length=200)
    rated = models.CharField(max_length=200, choices=RATING)
    genre = models.CharField(max_length=200)
    movie_image = models.ImageField(upload_to = 'image/')
    movie_link = models.CharField(max_length=200)
    movie_description = models.TextField()
    movie_rating = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)



    def __str__(self):
        return self.movie_name



