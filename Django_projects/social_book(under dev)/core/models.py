from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.CharField(max_length=50)
    bio = models.TextField(max_length=255, blank=True)
    profile_img = models.ImageField(verbose_name='profile image', upload_to='profile_images', default='blank-profile.bmp')
    create_date = models.DateTimeField(verbose_name="date created")
    location = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.user.username