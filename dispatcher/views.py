from django.http import request
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from dispatcher.serializers import *
from dispatcher.dispatchers import send_email


@api_view()
def get_auth_token(request):
    """
    Endpoint responds with an access token, to be used when making requests to
    authenticated endpoints.
    """

    # implement jwt access tokens.
    pass

@api_view(['POST'])
def welcome_message(request):
    """
    Endpoint sends welcome messages to receipients.
    """

    request_serializer = APIRequestSerializer(data=request.data)
    request_serializer.is_valid(raise_exception=True)

    api_request = request_serializer.validated_data
    data_serializer = WelcomeMessageSerializer(data=api_request['data'])
    data_serializer.is_valid(raise_exception=True)

    response = send_email('welcome_message', api_request)

    return response

@api_view(['POST'])
def new_booking_learner(request):
    """
    Endpoint notifies a mentor of a learner's request to book their serivces.
    """

    request_serializer = APIRequestSerializer(data=request.data)
    request_serializer.is_valid(raise_exception=True)

    api_request = request_serializer.validated_data
    data_serializer = BookingSerializer(data=api_request['data'])
    data_serializer.is_valid(raise_exception=True)

    response = send_email('learner_booking', api_request)
    
    return response

@api_view(['POST'])
def new_booking_mentor(request):
    """
    Endpoint sends mentor contact information to learner upon a request to
    book such mentor's services.
    """

    request_serializer = APIRequestSerializer(data=request.data)
    request_serializer.is_valid(raise_exception=True)

    api_request = request_serializer.validated_data
    data_serializer = BookingSerializer(data=api_request['data'])
    data_serializer.is_valid(raise_exception=True)

    response = send_email('mentor_booking', api_request)

    return response
