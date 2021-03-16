from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('api.versions.api_version_1'))
]
