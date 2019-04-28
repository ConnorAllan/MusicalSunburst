from django.db import models    

# Create your models here.
class Artists(models.Model):
    id = models.IntegerField(default=0)
    pmkArtist = models.TextField(max_length=50, primary_key=True)
    fldName = models.TextField(max_length=21)
    fldLocation = models.TextField(max_length=70)

    def __str__(self):
        return self.fldName

class Songs(models.Model):
    id = models.IntegerField(default=0)
    pmkSong = models.TextField(max_length=21, primary_key=True)
    fnkArtist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    fldTerms = models.TextField(max_length=30)
    fldTitle = models.TextField(max_length=100)
    fldYear = models.IntegerField(default=0000)

    def __str__(self):
        return self.fldTitle

class Releases(models.Model):
    id = models.IntegerField(default=0)
    pmkRelease = models.IntegerField(default=0, primary_key=True)
    fnkArtist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    fnkSong = models.ForeignKey(Songs, on_delete=models.CASCADE)
    fldName = models.TextField(max_length=101)

    def __str__(self):
        return self.fldName
