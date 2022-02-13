from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .address import views as address_views
from .user import views as user_views


urlpatterns = [
    path("addresses/", address_views.AddressList.as_view(), name="address-list"),
    path(
        "addresses/batch-deletion",
        address_views.AddressBatchDeletion.as_view(),
        name="address-batch-deletion",
    ),
    path(
        "addresses/<int:pk>/",
        address_views.AddressDetail.as_view(),
        name="address-detail",
    ),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "user/",
        user_views.UserSelfDetail.as_view(),
        name="user-self-detail",
    ),
]
