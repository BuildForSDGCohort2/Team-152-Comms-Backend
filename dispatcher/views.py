from django.http import request
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response

from dispatcher.serializers import *
from dispatcher.dispatchers import send_email
from dispatcher.models import TempToken


@api_view(['POST'])
def register(request):
    """Endpoint responds with an access token, to be used when making
    requests to authenticated endpoints.
    """
    serializer = AuthRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    user = User.objects.create_user(
        username=data['email'],
        email=data['email'],
        password=data['password']
    )

    temp_token = TempToken.objects.create(user=user)
    context = {
        'to': data['email'],
        'temp_token': temp_token.key
    }
    send_email('registeration', context=context)

    return Response({'detail': 'Continue registeration from the email sent to you.'})
    # return Response()


@api_view(['POST'])
def obtain_token(request):
    """Endpoint confirms authentication credentials and issues an access token.
    """

    pass

@api_view(['POST'])
def verify_token(request, temp_token):
    """Endpoint verifies a request to obtain a new token or refresh one assigned to
    an account.
    """

    pass

@api_view(['POST'])
def refresh_token(request):
    """Endpoint reissues access tokens to an account.
    """

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
