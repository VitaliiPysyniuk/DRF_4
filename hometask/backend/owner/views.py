from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    CreateAPIView, get_object_or_404

from .models import OwnerModel
from .serializers import OwnerSerializer
from company.serializers import CompanySerializer


class ListCreateOwnerView(ListCreateAPIView):
    queryset = OwnerModel.objects.all()
    serializer_class = OwnerSerializer


class RetrieveUpdateDestroyOwnerView(RetrieveUpdateDestroyAPIView):
    queryset = OwnerModel.objects.all()
    serializer_class = OwnerSerializer


class CreateOwnerCompanyView(CreateAPIView):
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        owner = get_object_or_404(OwnerModel, pk=pk)
        serializer.save(owner=owner)



