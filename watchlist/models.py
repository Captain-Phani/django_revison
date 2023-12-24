from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    website=models.URLField(max_length=100)

    def __str__(self):
        return self.name

class Watchlist(models.Model):
    title=models.CharField(max_length=100)
    storyline=models.CharField(max_length=200)
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist',default=1)
    active=models.BooleanField(default=True)
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title