from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_url = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='avatars',blank=True)

    def __str__(self):
        return self.user.username