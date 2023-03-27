from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets  
from django.http import JsonResponse
import paypalrestsdk
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Q


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',

        '/api/products/upload/',

        '/api/products/<id>/reviews/',

        '/api/products/top/',
        '/api/products/<id>/',

        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>',


        '/api/themes/'
        '/api/themes/create/'
        '/api/themes/<update>/<id>'
        '/api/themes/delete/<id>'
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def addProducts(request):
    data = request.data
    print(data)
    try:
        genre = Genre.objects.get(_id=data['genre'])
        product = Product.objects.create(
            name = data['name'],
            image = data['image'],
            description = data['description'],
            genre = genre,
        )
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Test'}
        return Response(message)

@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Producted Deleted')

@api_view(["POST"])
def addGenres(request):
    serializer = GenreSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getGenres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getGenreProducts(request, pk):
    products = Product.objects.filter(Q(genre=pk))
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def editProduct(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)
    
    product.name = data['name']
    product.image = data['image']
    product.description = data['description']

    genre_id = data['genre']
    genre = get_object_or_404(Genre, _id=genre_id)
    product.genre = genre

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getThemes(request):
    theme = Theme.objects.all()
    serializer = ThemeSerializer(theme, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTheme(request, pk):
    theme = Theme.objects.get(_id=pk)
    serializer = ProductSerializer(theme, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def editTheme(request, pk):
    data = request.data
    theme = Theme.objects.get(_id=pk)
    
    theme.name = data['name']
    theme.image = data['image']
    theme.description = data['description']

    theme.save()

    serializer = ThemeSerializer(theme, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def addTheme(request):
    data = request.data
    print(data)
    try:
        theme = Theme.objects.create(
            name = data['name'],
            image = data['image'],
            description = data['description'],
        )
        serializer = ThemeSerializer(theme, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Test'}
        return Response(message)
    
@api_view(['DELETE'])
def deleteTheme(request, pk):
    theme = Theme.objects.get(_id=pk)
    theme.delete()
    return Response('Producted Deleted')