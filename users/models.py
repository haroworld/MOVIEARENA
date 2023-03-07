from random import choices
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    PROFILE_TYPE = (
        ('Kids', 'Kids'),
        ('Adult', 'Adult')
    )
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, null=True,blank=True)
    username = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to = 'images/profileImage/', default = 'images/profileImage/user-default.png')
    profileType = models.CharField(max_length=200, choices=PROFILE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)



    def __str__(self):
        return self.firstname

    class Meta:
        ordering = ['created']

