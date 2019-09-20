from django.db import models
from django.utils import timezone
from datetime import datetime
from django.conf import settings 
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author  = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    image   = models.ImageField(default='default.png', blank=True)
    caption = models.TextField()
    likes   = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    created_date = models.DateTimeField(default=timezone.now)
    saved   = models.BooleanField(default=False)  

    def get_absolute_url(self):
        return reverse('insta:post_detail', kwargs={"id":self.id})
    
    def __str__(self):
        return self.caption 