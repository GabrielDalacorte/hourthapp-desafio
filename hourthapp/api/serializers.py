from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from hourthapp.models import HourthApp


class HourthAppSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):


    class Meta:
        model = HourthApp
        fields = ("id", "product", 'insertion_date',)
