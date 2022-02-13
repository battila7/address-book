from django.urls import path

from .address import views as address_views

urlpatterns = [
    path("addresses/", address_views.AddressList.as_view(), name="address-list"),
    path(
        "addresses/<int:pk>/",
        address_views.AddressDetail.as_view(),
        name="address-detail",
    ),
]
