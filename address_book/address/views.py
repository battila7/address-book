from rest_framework import generics, views as rest_views, response, status

from .models import Address
from .serializers import AddressSerializer, AddressBatchDeletionRequestSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressBatchDeletion(rest_views.APIView):
    def post(self, request):
        serializer = AddressBatchDeletionRequestSerializer(request.data)
        ids = serializer.data["ids"]

        Address.objects.filter(id__in=ids).delete()

        return response.Response(status=status.HTTP_204_NO_CONTENT)
