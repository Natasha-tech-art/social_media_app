from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/', include('users.urls')),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
]