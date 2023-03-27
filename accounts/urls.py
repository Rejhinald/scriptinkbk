from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.registerUser, name="sign_up"),
    path('updateuser/', views.updateUserProfile, name="update"),
    path('updateuserinfo/<str:pk>', views.updateUserInfo, name="update-info"),
    path('updatepayment/', views.payment, name="payment"),
    path('cancelsubscription/', views.cancelSubscription, name="cancelsub"),
    path('cancelsubscription/<str:pk>', views.cancelSubscriptionUser, name="cancelsub1"),
    path('subscriptionId/', views.storeSubscriptionId, name="subscriptionId"),
    path('userlist/', views.getUsers, name="getusers"),
    path('profile/', views.getUserProfile, name="user-profile"),
    path('user/<str:pk>', views.getUserInfo, name="user-info"),
    # path('mylist/<str:pk>', views.getMyUserMovieList, name="mylist"),
]