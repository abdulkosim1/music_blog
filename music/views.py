from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.models import Music
from music.serializers import MusicSerializers

# Create your views here.

@api_view(['GET'])
def get_hello(request):
    return Response('Hello word')

@api_view(['GET'])
def get_musics(request):
    musics = Music.objects.all()
    serializer = MusicSerializers(musics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_song(request, id):
    try:
        song = Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response('net takoy pesni')
    serializer = MusicSerializers(song, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_music(request):
    # print(request.data)
    serializer = MusicSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)