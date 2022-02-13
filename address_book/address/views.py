from rest_framework import generics, views as rest_views, response, status, permissions
from drf_yasg.utils import swagger_auto_schema

from .models import Address
from .serializers import AddressSerializer, AddressBatchDeletionRequestSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    """View to perform RUD operations on individual Addresses."""

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Retrieve Address

        Retrieves a single address specified by its unique identifier.
        """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update Address

        Updates a single address specified by its unique identifier. The updated
        fields can be set via the appropriate body fields, where all fields are **required**.
        """
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Partial Update Address

        Updates a single address specified by its unique identifier. The updated
        fields can be set via the appropriate body fields, where all fields are **optional**.
        """
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete Address

        Deletes a single address specified by its unique identifier.
        """
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Address.objects.none()

        return Address.objects.filter(owner=self.request.user)


class AddressList(generics.ListCreateAPIView):
    """View to create a new Address and list the available ones."""

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Explicitly setting which fields are available for filtering. For example,
    # created_at is excluded.
    filterset_fields = (
        "title",
        "country",
        "city",
        "state",
        "zip_code",
        "address_line_one",
        "address_line_two",
    )

    def get(self, request, *args, **kwargs):
        """List Addresses

        Lists the available addresses of the currently authenticated user.

        This endpoint is filtered, use the appropriate query parameters to filter
        the results returned. The filters are AND-ed together.

        Pagination is also available with a page size of 10.
        """
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Create Address

        Creates a new Address and assigns it to the currently authenticated user.
        """
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Address.objects.none()

        return Address.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AddressBatchDeletion(rest_views.APIView):
    """View to delete multiple Addresses at the same time as required.

    As the requirement was to create a RESTful API, I tried to implement
    a RESTful way of batch deletion. My thought process was as follows:
      * `DELETE /addresses?id=1&id=2&id=3` seems nice, as it uses the
        semantically correct `DELETE` verb and the friendly addresses endpoint,
        however, at the same time, is ugly, because it is essentially OR-ing
        together identifiers to create a non-existent, merged resource.
      * `DELETE /addresses` with a body of `{ "ids": [1, 2, 3] }` is not the
        most elegant way of solving things, as sending a body along with a `DELETE`
        request is generally discouraged.
      * That leaves us with the creation of a virtual resource, one that does not
        really exist, and most certainly is not part of our problem domain. Thus, I created
        `POST /addresses/batch-deletion` where one can submit a deletion request and immediately
        get back the result. In my opinion, this endpoint is correct REST, as it is essentially
        creating a new task (hence the `POST`), which resolves instantenously. If we expected
        deletion to take longer, we could even provide an appropriate `GET`-table endpoint where
        clients could check the deletion progress.
    """

    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        responses={204: None}, request_body=AddressBatchDeletionRequestSerializer
    )
    def post(self, request):
        """Batch Delete Addresses

        Sends a new batch deletion request marking the specified Addresses as deleted.
        """
        serializer = AddressBatchDeletionRequestSerializer(request.data)
        ids = serializer.data["ids"]

        Address.objects.filter(owner=request.user, id__in=ids).delete()

        return response.Response(status=status.HTTP_204_NO_CONTENT)
