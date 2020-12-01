from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import UpdateOwnProfile


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    


class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer
    
    def create(self, request):

        return ObtainAuthToken().post(request)


# class ChangePasswordView(viewsets.ModelViewSet):
    
#         serializer_class = UserProfileSerializer
#         queryset = UserProfile.objects.all().get('password')
#         permission_classes = (IsAuthenticated,)

    # def post(self, request):
    #     serializer = PasswordSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     user = request.user
    #     user.set_password(serializer.data['password'])
    #     user.save()

    #     return Response(status=status.HTTP_200_OK)