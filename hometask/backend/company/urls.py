from django.urls import path

from .views import ListCreateCompanyView, RetrieveUpdateDestroyCompanyView, CreateCompanyEmployeeView

urlpatterns = [
    path('', ListCreateCompanyView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyCompanyView.as_view()),
    path('<int:pk>/employee/', CreateCompanyEmployeeView.as_view())
]
