from datetime import timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404


from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action


from .models import Product
from .serializers import ProductSerializers




    # @action(detail=False, methods=['get'])
    # def new(self, request, pk=None):
    #     t = request.GET.get('t')
    #     queryset = self.get_queryset()
    #     start_time = timezone.now() - timedelta(minutes=5)
    #     queryset = queryset.filter(created_at__gt=start_time)
    #     serializer = ProductSerializers(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)



class ProductViewSet(viewsets.ModelViewSet):
        serializer_class = ProductSerializers
        queryset = Product.objects.all()