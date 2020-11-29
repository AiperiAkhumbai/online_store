from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Category
from .serializers import CategorySerializers



class CategoryViewSet(viewsets.ModelViewSet):
        serializer_class = CategorySerializers
        queryset = Category.objects.all()
        
        def get_permissions(self):
            if self.action == 'list':
                permission_classes = [AllowAny]
            else:
                permission_classes = [IsAdminUser]
            return [permission() for permission in permission_classes]