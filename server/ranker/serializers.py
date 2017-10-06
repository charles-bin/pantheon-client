""" Serializer for games. """

from ranker.models import Game
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = ('id', 'title', 'image', 'description', 'developer', 'genre', 'published', 'rank')
