""" Views handle how Django deals with API requests (GET, POST, PUT, DELETE) """
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ranker.models import Manga
from ranker.serializers import MangaSerializer
from django.http import JsonResponse
from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError

class MangaList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    """
    List all mangas, or creates a new manga instance.
    """
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

    def get(self, request, *args, **kwargs):
        """
        Fetches and returns list of all available Manga.

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
            Response object with a list of all manga objects

        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Creates a new manga instance.

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

class MangaDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    """
    Retreive, Update, or Delete a manga instance.
    """
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

    def get(self, request, *args, **kwargs):
        """
        Retrieves an individual manga instance object.

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
            Response object with specified manga instance

        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Updates an individual manga instance object.

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
        Deletes an individual manga instance object.

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
        return self.destroy(request, *args, **kwargs)
