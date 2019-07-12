from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from django.core.paginator import Paginator
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class AppAuth(APIView):

    # @swagger_auto_schema(
    #     responses={
    #         200: serializers.ResponseMatchListGet(many=True)
    #     },
    #     tags=[
    #         "Match"
    #     ],
    #     operation_summary='Match List',
    #     security=[],
    #     query_serializer=serializers.RequestMatchListGet
    # )
    def get(self, request, version=1, user=None, *args, **kwargs):
        pass
        # else:
        #     return Response(
        #         {
        #             "message": serializer.errors
        #         },
        #         status=status.HTTP_400_BAD_REQUEST
        #     )
