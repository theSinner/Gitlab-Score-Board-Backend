from django.shortcuts import redirect, resolve_url
from rest_framework import status
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from app.auth import get_server
from app.models import Application
from .utils import slugify_name
from user.models import User
from rest_framework.authtoken.models import Token
# Create your views here.


class UserAuth(APIView):

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
        serializer = serializers.RequestUserAuth(
            data=request.query_params
        )
        if serializer.is_valid():
            application = Application.find_application(
                serializer.validated_data['application_id']
            )
            if application:
                return redirect(get_server(
                    application.url,
                    application.application_id,
                    application.secret_token
                ).authorize(
                        redirect_uri='%s?application_id=%s' % (
                            request.build_absolute_uri(
                                reverse("user_auth_done")
                            ),
                            application.application_id
                        ),
                        state=request.build_absolute_uri(
                            reverse("user_auth")
                        ),
                        scope=[
                            'read_user',
                            'api',
                            'profile',
                            'openid',
                            'read_repository'
                        ]
                    )
                )
            else:
                return Response(
                    {
                        "message": "Application not found."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        else:
            return Response(
                {
                    "message": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class UserAuthDone(APIView):

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
        serializer = serializers.RequestUserAuthDone(
            data=request.query_params
        )
        if serializer.is_valid():
            application = Application.find_application(
                serializer.validated_data['application_id']
            )
            if application:
                res = get_server(
                    application.url,
                    application.application_id,
                    application.secret_token
                ).request_token(
                    redirect_uri='%s?application_id=%s' % (
                        request.build_absolute_uri(
                            reverse("user_auth_done")
                        ),
                        application.application_id
                    ),
                    code=serializer.validated_data['code'],
                )
                user = User.get_user(
                    username=res.userinfo['nickname'],
                    application=application
                )
                if not user:
                    username = '%s__%s' % (
                        slugify_name(application.name),
                        res.userinfo['nickname']
                    )
                    user = User.add_user(
                        username,
                        res.userinfo['name'],
                        avatar=res.userinfo['picture'],
                        id_token=res.id_token,
                        access_token=res.access_token,
                        application=application,
                        app_username=res.userinfo['nickname'],
                        openid=res.id,
                    )
                token, created = Token.objects.get_or_create(user=user)
                res = {
                    'token': token.key,
                    'user': {

                    }
                }
                return Response(res, 200)
            else:
                return Response(
                    {
                        "message": "Application not found."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        else:
            return Response(
                {
                    "message": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
