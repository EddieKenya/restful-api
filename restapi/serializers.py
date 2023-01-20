from rest_framework import serializers
from .models import Posts
from rest_framework.serializers import SerializerMethodField

class PostformSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Posts
        fields = '__all__'

    def get_user(self, obj):
        return str(obj.user.username)

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['title',
                 'content',
                 'image'
        ]
