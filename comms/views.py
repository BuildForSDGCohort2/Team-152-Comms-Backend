
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def root_view(request):
    """
    Root API View
    """

    return Response(
        {
            'detail': 'This API handles communication for the Team-152 Project.'
        }
    )