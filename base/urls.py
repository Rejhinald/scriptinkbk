from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api/', views.getRoutes, name="routes"),
    path('api/products', views.getProducts, name="products"),
    path('api/genres', views.getGenres, name="genres"),
    path('api/genres/create', views.addGenres, name="addgenres"),
    path('api/genreproducts/<str:pk>', views.getGenreProducts, name="genreproducts"),
    # path('api/genreproducts2/<str:pk>', views.getGenre2Products, name="genreproducts2"),
    # path('api/genreproducts3/<str:pk>', views.getGenre3Products, name="genreproducts3"),
    path('api/products/create', views.addProducts, name="addproducts"),
    path('api/products/delete/<str:pk>/', views.deleteProduct, name="product-delete"),
    path('api/products/<str:pk>', views.getProduct, name="product"),
    path('api/products/update/<str:pk>/', views.editProduct, name="product-edit"),

    path('api/themes', views.getThemes, name="themes"),
    path('api/themes/create', views.addTheme, name="addtheme"),
    path('api/themes/delete/<str:pk>/', views.deleteTheme, name="theme-delete"),
    path('api/themes/<str:pk>', views.getTheme, name="theme"),
    path('api/themes/update/<str:pk>/', views.editTheme, name="theme-edit"),
]