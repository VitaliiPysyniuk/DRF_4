from rest_framework.serializers import ModelSerializer

from .models import OwnerModel
from company.serializers import CompanySerializer


class OwnerSerializer(ModelSerializer):
    companies = CompanySerializer(many=True, required=False)

    class Meta:
        model = OwnerModel
        fields = ['id', 'name', 'surname', 'capital', 'email', 'password',  'is_superuser',
                  'companies']
        extra_kwargs = {
            'id': {'read_only': True},
            'is_superuser': {'read_only': True}
        }

    def create(self, validated_data):
        owner = OwnerModel.objects.create_standard_owner(**validated_data)
        owner.save()
        return owner

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.capital = validated_data.get('capital', instance.capital)
        instance.email = validated_data.get('email', instance.email)
        new_password = validated_data.get('password')
        if new_password:
            instance.set_password(new_password)
        instance.save()
        return instance





