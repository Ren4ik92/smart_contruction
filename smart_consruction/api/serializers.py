from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..news.models import PostNews

User = get_user_model()


class PostNewsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PostNews
        extra_kwargs = {'image': {'required': False}}
