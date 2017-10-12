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
    serializer_class = GameSerializer

    def get_queryset(self):
        """
        Optionally restricts the queryset through given filter Parameters.
        """
        queryset = Game.objects.all()
        filter_title = self.request.GET.get('filter-title', None)
        if filter_title:
            queryset = queryset.filter(title__contains=filter_title)
        filter_description = self.request.GET.get('filter-description', None)
        if filter_description:
            queryset = queryset.filter(description__contains=filter_description)
        filter_developer = self.request.GET.get('filter-developer', None)
        if filter_developer:
            queryset = queryset.filter(developer__contains=filter_developer)
        filter_genre = self.request.GET.get('filter-genre', None)
        if filter_genre:
            queryset = queryset.filter(genre__contains=filter_genre)
        filter_before = self.request.GET.get('filter-before', None)
        if filter_before:
            queryset = queryset.filter(published__lte=filter_before)
        filter_after = self.request.GET.get('filter-after', None)
        if filter_after:
            queryset = queryset.filter(published__gte=filter_after)
        filter_rank_lt = self.request.GET.get('filter-rank-lt', None)
        if filter_rank_lt:
            queryset = queryset.filter(rank__lte=filter_rank_lt)
        filter_rank_gt = self.request.GET.get('filter-rank-gt', None)
        if filter_rank_gt:
            queryset = queryset.filter(rank__gte=filter_rank_gt)
        return queryset

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
