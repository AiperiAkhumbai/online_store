from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializers



class CategoryViewSet(viewsets.ModelViewSet):
        serializer_class = CategorySerializers
        queryset = Category.objects.all()