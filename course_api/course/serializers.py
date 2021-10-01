from django.db.models import fields
from rest_framework import serializers
from .models import Course

# class CourseSerializer(serializers.ModelSerializer):
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        # fields = ('id', 'name', 'language', 'price')
        fields = ('id', 'url', 'name', 'language', 'price')