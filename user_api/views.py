from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from user_api.models import Integer as IntegerModel
from user_api.serializers import IntegerSerializer, NextIntegerSerializer


class Integer(APIView):

    permission_classes = IsAuthenticated,
    serializer_class = IntegerSerializer

    def get(self, request):
        user = self.request.user.customuser
        serializer = self.serializer_class(user, many=False)
        return Response(serializer.data)

    def put(self, request):
        user = self.request.user.customuser
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NextInteger(APIView):

    permission_classes = IsAuthenticated,
    serializer_class = NextIntegerSerializer

    def get(self, request):
        user = self.request.user.customuser
        serializer = self.serializer_class(user, many=False)
        return Response(serializer.data)