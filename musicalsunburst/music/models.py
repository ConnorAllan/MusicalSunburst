from django.db import models

# Create your models here.

class Artists(models.Model):
    index = models.IntegerField()
    pmkArtist = models.TextField(max_length=50)
    fldName = models.TextField(max_length=20)
    fldLocation = models.TextField(max_length=70)

    
class Songs(models.Model):
    index = models.IntegerField()
    pmkSong = models.TextField(max_length=20)
    fnkArtist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    fldTerms = models.TextField(max_length=30)
    fldTitle = models.TextField(max_length=100)
    fldYear = models.IntegerField()

    def Song(self):
        return self.song_title

class Releases(models.Model):
    index = models.IntegerField()
    pmkRelease = models.IntegerField()
    fnkArtist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    fnkSong = models.ForeignKey(Songs, on_delete=models.CASCADE)
    fldName = models.TextField(max_length=100)

    def __str__(self):
        return self.album_title+'-'+self.artist
