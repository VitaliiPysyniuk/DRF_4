from django.urls import path

from .views import ListCreateCarView

urlpatterns = [
    path('', ListCreateCarView.as_view())
]
