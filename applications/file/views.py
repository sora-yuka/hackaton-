from django.shortcuts import render
from .models import File
from rest_framework import viewsets
from .sersializers import FileSerializer


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()