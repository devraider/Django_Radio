from django.contrib.auth.models import User, Group
from .models import TrackModel, SpotifyModel
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SpotifyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyModel
        fields = '__all__'


class TrackModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackModel
        fields = '__all__'
