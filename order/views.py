from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import  IsAdminUser, IsAuthenticated

from .models import Order
from .serializers import OrderSerializers


class OrderViewSet(viewsets.ModelViewSet):

        serializer_class = OrderSerializers
        queryset = Order.objects.all()
        permission_classes = (IsAuthenticated,)
           