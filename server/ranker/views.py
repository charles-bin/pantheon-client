""" Views handle how Django deals with API requests (GET, POST, PUT, DELETE) """
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ranker.models import Game
from ranker.serializers import GameSerializer
from django.http import JsonResponse
from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError

class GameList(mixins.ListModelMixin,
	            mixins.CreateModelMixin,
	            generics.GenericAPIView):
	"""
	List all games, or creates a new game instance.
	"""
	queryset = Game.objects.all()
	serializer_class = GameSerializer

	def get(self, request, *args, **kwargs):
		"""
		Fetches and returns list of all available games.

		Parameters
		----------
		request : request
		    Carries request data
		*args : tuple
		    List of additional arguments
		**kwargs : dictionary
		    Additional key-value argument pairs

		Returns
		-------
		Response
		    Response object with a list of all game objects

		"""
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		"""
		Creates a new game instance.

		Parameters
		----------
		request : request
		    Carries request data
		*args : tuple
		    List of additional arguments
		**kwargs : dictionary
		    Additional key-value argument pairs

		Returns
		-------
		Response
		    Response object with creation status

		"""
		return self.create(request, *args, **kwargs)

class GameDetail(mixins.RetrieveModelMixin,
	              mixins.UpdateModelMixin,
	              mixins.DestroyModelMixin,
	              generics.GenericAPIView):
    """
    Retreive, Update, or Delete a game instance.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get(self, request, *args, **kwargs):
    	"""
    	Retrieves an individual game instance object.

    	Parameters
    	----------
    	request : request
    	    Carries request data
    	*args : tuple
    	    List of additional arguments
    	**kwargs : dictionary
    	    Additional key-value argument pairs

    	Returns
    	-------
    	Response
    	    Response object with specified game instance

    	"""
    	return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
    	"""
    	Updates an individual game instance object.

    	Parameters
    	----------
    	request : request
    	    Carries request data
    	*args : tuple
    	    List of additional arguments
    	**kwargs : dictionary
    	    Additional key-value argument pairs

    	Returns
    	-------
    	Response
    	    Response object with update status

    	"""
    	return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
    	"""
    	Deletes an individual game instance object.

    	Parameters
    	----------
    	request : request
    	    Carries request data
    	*args : tuple
    	    List of additional arguments
    	**kwargs : dictionary
    	    Additional key-value argument pairs

    	Returns
    	-------
    	Response
    	    Response object with delete status

    	"""
    	self.destroy(request, *args, **kwargs)
