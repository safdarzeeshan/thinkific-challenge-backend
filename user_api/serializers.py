from rest_framework import serializers
from user_api.models import *
# from rest_auth.serializers import UserDetailsSerializer


class IntegerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('current_integer',)


class NextIntegerSerializer(serializers.ModelSerializer):

    next_integer = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('next_integer', )

    def get_next_integer(self, user):

        next_integer = user.current_integer + 1
        return next_integer
