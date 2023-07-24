from rest_framework import serializers
from .models import Comment, Fav

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class FavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fav
        fields = '__all__'