from django.urls import path

from .views import ProfileDetailView, RegisterView, UserSearchView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('search/users/', UserSearchView.as_view(), name='user-search'),
]