from rest_framework import status
from rest_framework.generics import ListCreateAPIView, get_object_or_404, \
    RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CompanyModel
from .serializers import CompanySerializer
from employee.models import EmployeeModel
from employee.serializers import EmployeeSerializer


class ListCreateCompanyView(ListCreateAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self, **kwargs):
        queryset = CompanyModel.objects.all()
        city = self.request.query_params.get('city')
        if city:
            queryset = queryset.filter(city__iexact=city)
        return queryset


class RetrieveUpdateDestroyCompanyView(RetrieveUpdateDestroyAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer

    def perform_destroy(self, instance):
        employees_all = instance.employees.all()
        print(employees_all)
        data = {'is_employed': False}
        for employee in employees_all:
            serializer = EmployeeSerializer(employee, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        instance.delete()
        return Response(1, status=status.HTTP_204_NO_CONTENT)


class CreateCompanyEmployeeView(CreateAPIView):
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        print(pk)
        company = get_object_or_404(CompanyModel, pk=pk)
        serializer.save(company=company)


