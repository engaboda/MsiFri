from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=300)
    album_title= models.CharField(max_length=300)
    genr = models.CharField(max_length=350)
    album_logo = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse('music:detail' , kwargs={'pk':self.id})


    def __unicode__(self):
        return self.artist+"--------" + self.album_title +" ----- "+ self.album_logo

class Song(models.Model):
    album = models.ForeignKey(Album , on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    fiel_type = models.CharField(max_length=30)
    is_favorite = models.BooleanField(default=False)



    def __unicode__(self):
        return self.name

class User(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)