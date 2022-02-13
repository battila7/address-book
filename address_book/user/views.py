from rest_framework import views as rest_views, response, permissions
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserSerializer


class UserSelfDetail(rest_views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(responses={200: UserSerializer})
    def get(self, request):
        """Get Current User

        Retrieves the currently authenticated user.
        """
        serializer = UserSerializer(request.user)

        return response.Response(serializer.data)
