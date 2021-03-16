from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('api.api_version_1'))
]
