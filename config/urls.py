from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


def api_root(request):
    return JsonResponse({
        'message': 'API is running',
        'routes': [
            '/api/register/',
            '/api/profiles/<id>/',
            '/api/search/users/',
            '/api/posts/',
        ],
    })


urlpatterns = [
    path('', api_root, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('posts.urls')),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
]