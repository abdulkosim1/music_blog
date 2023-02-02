from rest_framework import serializers
from music.models import Music


class MusicSerializers(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'