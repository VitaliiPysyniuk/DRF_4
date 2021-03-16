from django.urls import path

from .views import ListCreateUserView, CreateUserCarView

urlpatterns = [
    path('', ListCreateUserView.as_view()),
    path('<int:pk>/cars/', CreateUserCarView.as_view())
]
