from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import EmployeeModel
from .serializers import EmployeeSerializer


class ListCreateEmployeeView(ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class RetrieveUpdateDestroyEmployeeView(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
