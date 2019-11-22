from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import User
from django.contrib import admin
admin.autodiscover()
from rest_framework import viewsets
from api.serializers import UserSerializer
from django.http import JsonResponse
from rest_framework import status
from oauth2_provider.models import AccessToken
from django.contrib.auth.models import User as AuthUser



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    permission_classes = ()
    authentication_classes = ()

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['GET'], url_path='get-current-userinfo')
    def get_current_userinfo(self, request):
        access_token = request.META["HTTP_AUTHORIZATION"][7:]
        access_token_object = AccessToken.objects.get(token=access_token)
        user = access_token_object.user
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['password'] = make_password(data['password'])
        data['is_active'] = True
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['GET'], url_path='get-current-user-info')
    def get_current_userinfo(self, request):
        access_token = request.META["HTTP_AUTHORIZATION"][7:]
        access_token_object = AccessToken.objects.get(token=access_token)
        user = access_token_object.user
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)