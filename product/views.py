from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Max, Min
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Product
from .serializers import ProductSerializers


class ProductSetPagination(PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):
        prices = Product.objects.aggregate(max=Max('price'), min=Min('price'))
        return Response({
            'meta': {
                'page': self.page.number,
                'has_prev': self.page.has_previous(),
                'has_next': self.page.has_next(),
                'min_price': prices['min'],
                'max_price': prices['max'],
            },
            'data': data
        })


class ProductViewSet(viewsets.ModelViewSet):

        pagination_class = ProductSetPagination
        serializer_class = ProductSerializers
        queryset = Product.objects.all()
        filter_backends = (filters.SearchFilter,)
        search_fields = ('name', 'category','price')

        def get_permissions(self):
            if self.action == 'list':
                permission_classes = [AllowAny]
            else:
                permission_classes = [IsAdminUser]
            return [permission() for permission in permission_classes]

        