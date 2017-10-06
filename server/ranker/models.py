""" Data model for Game objects. """

from django.db import models

class Game(models.Model):
    """
    Data Model for game
    """
    title = models.CharField(max_length=100, blank=True, default='')
    image = models.CharField(max_length=200, blank=True, default='')
    description = models.CharField(max_length=200, blank=True, default='')
    developer = models.CharField(max_length=100, blank=True, default='')
    genre = models.CharField(max_length=200, blank=True, default='[]')
    published = models.DateField(blank=True, default='')
    rank = models.IntegerField(blank=True, default=0)

    def __str__(self):
        """
        Overriding default representation for readability.
        Displays game object by title and rank.
        """
        return "Title:{0}, Rank:{1}".format(self.title, self.rank)

    def clean(self):
        """
        Overriding Django's Model Validation method.
        """
        # sets initial rank to lowest possible
        if self.rank == 0:
            self.rank = len(Game.objects.all()) + 1

    def save(self, *args, **kwargs):
        """
        Overriding Django's Model Save method to call clean.
        """
        self.full_clean()
        return super(Game, self).save(*args, **kwargs)

    class Meta:
        """
        Meta class used to order game instances by rank.
        """
        ordering = ('rank',)
