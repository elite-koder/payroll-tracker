from rest_framework import viewsets, mixins, exceptions
from rest_framework.permissions import AllowAny
from user.serializers import LoginSerializer, TokenSerializer
from rest_framework import authentication
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response

class LoginView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.pop('password')
        username = serializer.validated_data.pop('username')
        user = authentication.authenticate(
            request=request, 
            username=username, 
            password=password)
        if not user:
            raise exceptions.AuthenticationFailed('Invalid Credentials')
        token, created = Token.objects.get_or_create(user=user)
        serializer = TokenSerializer(token)
        headers = self.get_success_headers(serializer.data)
        print(headers)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        