from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    #api
    path('api/', views.getRoutes, name="routes"),

    #genres
    path('api/genres', views.getGenres, name="genres"),
    path('api/genres/<str:pk>', views.getGenre, name="genre"),
    path('api/genres/create', views.addGenres, name="addgenres"),
    path('api/genreproducts/<str:pk>', views.getGenreProducts, name="genreproducts"),

    #tiers
    path('api/tiers', views.getTiers, name="tiers"),
    path('api/tiers/create', views.addTier, name="addtier"),
    path('api/tierproducts/<str:pk>', views.getTierProducts, name="tierproducts"),

    #product
    path('api/products', views.getProducts, name="products"),
    path('api/products/create', views.addProducts, name="addproducts"),
    path('api/products/delete/<str:pk>/', views.deleteProduct, name="product-delete"),
    path('api/products/<str:pk>', views.getProduct, name="product"),
    path('api/products/update/<str:pk>/', views.editProduct, name="product-edit"),

    #likes
    path('api/products/<int:product_id>/like/', views.like_product, name='like_product'),
    path('api/products/<int:product_id>/unlike/', views.unlike_product, name='unlike_product'),
    
    #comments
    path('products/<int:product_id>/comments/', views.comment_list, name='list_comment'),
    path('products/<int:product_id>/comments/add/', views.add_comment, name='add_product'),
    path('products/<int:product_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_product'),
]
