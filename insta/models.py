from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)
    published_date = models.CharField()

    def __str__(self):
        return self.caption
    @property
    def published(self):
        created_dates = self.created_date.replace(tzinfo=None)
        Now = datetime.now()
        Now = Now.replace(microsecond=0)
        time_difference = Now - created_dates
        if time_difference.days == 0:
            if int(time_difference.seconds/3600) == 0:
                self.published_date = str(int(time_difference.seconds/60)) + " MINUTES AGO"
            else:
                self.published_date = str(int(time_difference.seconds/3600)) + " HOURS AGO"
        else:
            self.published_date = str(int(time_difference.days)) + " DAYS AGO"   
        self.save()
        return self.published_date 
