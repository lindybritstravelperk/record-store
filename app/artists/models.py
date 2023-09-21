"""
Artist and Track models.
"""
from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Track(models.Model):
    artist = models.ForeignKey(Artist, related_name="tracks", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
