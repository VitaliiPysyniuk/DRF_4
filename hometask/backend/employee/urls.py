from django.urls import path

from .views import ListCreateEmployeeView, RetrieveUpdateDestroyEmployeeView

urlpatterns = [
    path('', ListCreateEmployeeView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyEmployeeView.as_view())
]
