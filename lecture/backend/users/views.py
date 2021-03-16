from rest_framework.generics import ListCreateAPIView, CreateAPIView, get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import UserSerializer
from cars.serializers import CarSerializer

UserModel = get_user_model()


class ListCreateUserView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class CreateUserCarView(CreateAPIView):
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        user_id = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=user_id)
        serializer.save(owner_id=user_id)




