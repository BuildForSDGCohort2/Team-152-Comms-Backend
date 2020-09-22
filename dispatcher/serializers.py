
from re import S
from rest_framework import serializers
from rest_framework.fields import MISSING_ERROR_MESSAGE
from rest_framework.serializers import Serializer


class APIRequestSerializer(Serializer):
    to = serializers.EmailField()
    data = serializers.JSONField()

class WelcomeMessageSerializer(Serializer):
    message = serializers.CharField(
        max_length=200,
        allow_blank=True
    )
    name = serializers.CharField()
    email = serializers.EmailField()

class BookingSerializer(Serializer):
    mentor_name = serializers.CharField(
        max_length=150
    )
    mentor_email = serializers.EmailField()
    learner_name = serializers.CharField(
        max_length=150
    )
    learner_email = serializers.EmailField()
    learner_phone = serializers.CharField(
        max_length=15
    )
    courses = serializers.ListField()
    message = serializers.CharField(
        max_length=200,
        allow_blank=True
    )
