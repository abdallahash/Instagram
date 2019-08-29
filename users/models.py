from django.db import models
from django.contrib.auth.models import User 
from PIL import Image 
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #CASCADE means if the user is deleted then delete the profile 
    profile_photo = models.ImageField(default='default_avatar.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=250)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        
        img = Image.open(self.profile_photo.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_photo.path)


    