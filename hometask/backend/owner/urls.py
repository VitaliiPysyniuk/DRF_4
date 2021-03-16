from django.urls import path

from .views import ListCreateOwnerView, RetrieveUpdateDestroyOwnerView, CreateOwnerCompanyView

urlpatterns = [
    path('', ListCreateOwnerView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyOwnerView.as_view()),
    path('<int:pk>/company/', CreateOwnerCompanyView.as_view())
]
