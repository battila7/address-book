from rest_framework import views as rest_views, response

from .serializers import UserSerializer


class UserSelfDetail(rest_views.APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)

        return response.Response(serializer.data)
