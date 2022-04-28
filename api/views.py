from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
# Create your views here.

@api_view(['GET'])
def get_routes(request):
    
    return Response('our api')

@api_view(['GET'])

def get_notes(request):
    notes = Note.objects.all()
    serialzer = NoteSerializer(notes, many=True)
    return Response(serialzer.data)

@api_view(['GET'])
def get_note(request, pk):
    notes = Note.objects.get(id=pk)
    serialzer = NoteSerializer(notes, many=False)
    return Response(serialzer.data)

