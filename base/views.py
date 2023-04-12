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
from rest_framework import status
from django.contrib.auth import get_user_model




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
    author_email = data['author']
    try:
        author = User.objects.get(email=author_email)
    except User.DoesNotExist:
        return Response({'error': 'Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    genre = Genre.objects.get(_id=data['genre'])
    tier = Tier.objects.get(id=data['tier'])
    product = Product.objects.create(
        name=data['name'],
        image=data['image'],
        short_description=data['short_description'],
        description=data['description'],
        genre=genre,
        author=author,
        tier=tier
    )
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)




@api_view(['DELETE'])
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
def getGenre(request, pk):
    genre = Genre.objects.get(_id=pk)
    serializer = GenreSerializer(genre, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getGenreProducts(request, pk):
    products = Product.objects.filter(Q(genre=pk))
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def addTier(request):
    serializer = TierSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getTiers(request):
    tiers = Tier.objects.all()
    serializer = TierSerializer(tiers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTierProducts(request, pk):
    products = Product.objects.filter(Q(tier=pk))
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    

@api_view(['PUT'])
def editProduct(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)

    product.name = data.get('name', product.name)
    product.image = data.get('image', product.image)
    product.short_description = data.get('short_description', product.short_description)
    product.description = data.get('description', product.description)

    genre_id = data.get('genre', None)
    if genre_id:
        try:
            genre = Genre.objects.get(_id=int(genre_id))
            product.genre = genre
        except Genre.DoesNotExist:
            return Response({'error': 'Genre does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    tier_id = data.get('tier', None)
    if tier_id:
        try:
            tier = Tier.objects.get(id=int(tier_id))
            product.tier = tier
        except Tier.DoesNotExist:
            return Response({'error': 'Tier does not exist'}, status=status.HTTP_404_NOT_FOUND)

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def like_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.likes += 1
    product.save()
    return Response({'likes': product.likes})

@api_view(['PUT'])
def unlike_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.likes -= 1
    product.save()
    return Response({'likes': product.likes})


@api_view(['GET'])
def comment_list(request, product_id):
    try:
        comments = Comment.objects.filter(product_id=product_id)
    except Comment.DoesNotExist:
        return Response({'error': 'Comments do not exist for the product'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request, product_id):
    data = request.data
    author_email = request.user.email
    try:
        author = User.objects.get(email=author_email)
    except User.DoesNotExist:
        return Response({'error': 'Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save(product_id=product_id, author=author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_comment(request, product_id, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id, product_id=product_id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)