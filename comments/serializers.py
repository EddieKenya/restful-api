from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from.models import Comments



class CommentSerializer(ModelSerializer):
    user = SerializerMethodField
    class Meta:
        model = Comments
        fields = '__all__'

    def comment_user( self, obj):
        return str(obj.user.username)