from api.models import User
from django.contrib import admin
admin.autodiscover()
from rest_framework import serializers

# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }
