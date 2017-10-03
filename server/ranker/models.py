""" Data model for Manga objects. """

from django.db import models

class Manga(models.Model):
    """
    Data Model for Manga
    """
    title = models.CharField(max_length=100, blank=True, default='')
    image = models.CharField(max_length=200, blank=True, default='')
    description = models.CharField(max_length=200, blank=True, default='')
    author = models.CharField(max_length=100, blank=True, default='')
    genre = models.CharField(max_length=200, blank=True, default='[]')
    published = models.DateField(blank=True, default='')
    rank = models.IntegerField(blank=True, default=0)

    def __str__(self):
        """
        Overriding default representation for readability.
        Displays manga object by title and rank.
        """
        return "Title:{0}, Rank:{1}".format(self.title, self.rank)

    class Meta:
        """
        Meta class used to order manga instances by rank.
        """
        ordering = ('rank',)
