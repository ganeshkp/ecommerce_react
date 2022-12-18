from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from base.models import Product
from base.serializers import ProductSerializer, UserSerializer, UserSerializerWithToken

from django.contrib.auth.hashers import make_password
from rest_framework import status

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAdminUser])
def getProduct(request, pk):
    # product=None

    # for i in products:
    #     if i['_id'] == pk:
    #         product = i
    #         break

    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)