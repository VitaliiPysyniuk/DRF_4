from rest_framework.generics import ListCreateAPIView

from .models import CarModel
from  .serializers import CarSerializer

class ListCreateCarView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
