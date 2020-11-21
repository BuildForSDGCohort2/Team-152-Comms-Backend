from django.db import models

from rest_framework.authtoken.models import Token


class TempToken(Token):
    status = models.CharField(max_length=300)
