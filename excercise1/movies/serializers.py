from rest_framework import serializers
from .models import Router
from django.contrib.auth.models import User


class RouterSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Router
        fields = ('id', 'sapid', 'hostname', 'macAddress','ipAddress', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel
    router = serializers.PrimaryKeyRelatedField(many=True, queryset=Router.objects.all())

    class Meta:
        model = User
        fields = ('ipAddress')
