"""
Serializers for the artists API.
"""
from rest_framework import serializers

from .models import Artist, Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['title']

class ArtistSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Artist
        fields = ['id', 'first_name', 'last_name', 'tracks']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks', [])
        artist = Artist.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(artist=artist, **track_data)
        return artist

    def update(self, artist, validated_data):
        tracks_data = validated_data.get('tracks', [])
        artist.first_name = validated_data.get('first_name', artist.first_name)
        artist.last_name = validated_data.get('last_name', artist.last_name)
        artist.save()
        Track.objects.filter(artist=artist).delete()
        for track_data in tracks_data:
            Track.objects.create(artist=artist, **track_data)
        return artist



