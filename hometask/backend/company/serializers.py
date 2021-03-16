from rest_framework.serializers import ModelSerializer

from .models import CompanyModel
from employee.serializers import EmployeeSerializer


class CompanySerializer(ModelSerializer):
    employees = EmployeeSerializer(many=True, required=False)

    class Meta:
        model = CompanyModel
        fields = ['id', 'name', 'country', 'city', 'employees', 'owner']
        read_only_fields = ['employees']

    def create(self, validated_data):
        company = CompanyModel.objects.create(**validated_data)
        return company


