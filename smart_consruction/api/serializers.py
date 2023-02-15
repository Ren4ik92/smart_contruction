from django.contrib.auth import get_user_model
from rest_framework import serializers
from vacancy.models import Vacancy
from news.models import PostNews

from rest_framework.validators import UniqueValidator


User = get_user_model()


class PostNewsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PostNews
        extra_kwargs = {'image': {'required': False}}


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'title', 'description', 'date_posted', 'date_expired', 'is_archived']
