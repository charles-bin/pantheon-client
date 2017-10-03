""" Serializer for data models (manga). """

from ranker.models import Manga
from rest_framework import serializers

class MangaSerializer(serializers.ModelSerializer):
    """
    Model serializer for manga objects.
    """
    class Meta:
        """
        Meta class used to describe model fields.
        """
        model = Manga
        fields = ('id', 'title', 'image', 'description', 'author', 'genre', 'published', 'rank')
