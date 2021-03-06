from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User



class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']



class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
