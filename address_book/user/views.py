from rest_framework import views as rest_views, response, permissions

from .serializers import UserSerializer


class UserSelfDetail(rest_views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)

        return response.Response(serializer.data)
