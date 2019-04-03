from django.db import models

# Create your models here.
class Artists(models.Model):
    pmkArtist = models.TextField(max_length=50)
    fldName = models.TextField(max_length=20)
    fldLocation = models.TextField(max_length=70)

class Songs(models.Model):
    pmkSong = models.TextField(max_length=20)
    fnkArtist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    fldTerms = models.TextField(max_length=30)
    fldTitle = models.TextField(max_length=100)
    fldYear = models.IntegerField(default=0)

class Releases(models.Model):
    pmkRelease = models.IntegerField(default=0)
    fnkArtist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    fnkSong = models.ForeignKey(Songs, on_delete=models.CASCADE)
    fldName = models.TextField(max_length=100)
