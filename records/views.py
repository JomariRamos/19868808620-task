from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from .models import Record 
from .serializers import RecordSerializer

# Create your views here.

class RecordModelViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer

    filterset_fields = ['created_at']
    ordering_fields = ('created_at',)

    def get_queryset(self):
        # This returns the records for the current user
        return Record.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)