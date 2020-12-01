from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Max, Min
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Product
from .serializers import ProductSerializers


''' Pagination by page -- 2 product in one page'''

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


''' Everybody can see list of products and Admin can do CRUD '''

class ProductViewSet(viewsets.ModelViewSet):

        serializer_class = ProductSerializers
        queryset = Product.objects.all()
        pagination_class = ProductSetPagination
        filter_backends = (filters.SearchFilter,)
        search_fields = ('name')

        def get_permissions(self):
            if self.action == 'list':
                permission_classes = [AllowAny]
            else:
                permission_classes = [IsAdminUser]
            return [permission() for permission in permission_classes]


        @action(detail=False, methods=['get'])         
        def search(self, request, pk=None):
            q = request.query_params.get('q')
            queryset = self.get_queryset()
            queryset = queryset.filter(Q(name__icontains=q) |
                                   Q(description__icontains=q))
            serializer = ProductSerializers(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        