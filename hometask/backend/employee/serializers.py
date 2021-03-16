from rest_framework.serializers import ModelSerializer

from .models import EmployeeModel


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ['id', 'name', 'surname', 'age', 'profession', 'is_employed',
                  'company']

    def create(self, validated_data):
        employee = EmployeeModel.objects.create(**validated_data)
        employee.save()
        return employee
