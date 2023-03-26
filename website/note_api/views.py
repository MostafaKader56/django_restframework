from django.shortcuts import render, HttpResponse
from .models import *
from django.shortcuts import redirect
from django.contrib.messages import constants as messages
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteModelSerializer
from rest_framework import viewsets


def name(request, nickname):
    return HttpResponse(f'Hellow {nickname}')


def showAll(request):
    notes = Note.objects.all()
    return render(request, 'index.html', context={'notes': notes})


def showOne(request, id):
    note = Note.objects.get(id=id)
    return render(request, 'note.html', context={'note': note})


def createOne(request):
    messages.add_message(request, messages.INFO, 'Hello world.')
    return HttpResponse(f'Hellow {request}')

@api_view(['GET'])
def responseWithJason(request):
    Jason = [
        {
            'name': 'Mostafa',
            'age': '4' 
        },
        {
            'name': 'Mostafa',
            'age': '24'
        },
        {
            'name': 'Mostafa',
            'age': '24'
        },
    ]
    return Response(Jason)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteModelSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def getNote (request,id):
    note = Note.objects.get(id=id)
    serializer = NoteModelSerializer(note)
    return Response(serializer.data)

@api_view(['POST'])
def createNote (request):
    serializer = NoteModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: Response(serializer.errors)


@api_view(['GET','PUT'])
def updateNote (request,idInput):
    note = Note.objects.get(id=idInput)
    serializer = NoteModelSerializer(note,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: return Response(serializer.errors)


@api_view(['GET'])
def deleteNote (request,idInput):
    note = Note.objects.get(id=idInput)
    note.delete()
    return Response('Note is deleted')

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteModelSerializer