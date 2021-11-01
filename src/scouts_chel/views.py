from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class ApiRoot(APIView):
    """
    View for API Root
    """
    def get(self, request, format=None):
        """
        Return list of API Root
        :param request: GET
        :return: API Root list
        """
        return Response({
            'persons': reverse('person-list', request=request, format=format),
        })