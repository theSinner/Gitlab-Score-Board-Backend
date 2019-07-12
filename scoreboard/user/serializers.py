from rest_framework import serializers


class RequestUserAuth(serializers.Serializer):
    application_id = serializers.CharField(required=True)


class RequestUserAuthDone(serializers.Serializer):
    code = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    application_id = serializers.CharField(required=True)
