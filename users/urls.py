from django.urls import path
from .views import ProfileDetailView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view()),
]

path(
    'profiles/<int:pk>/',
    ProfileDetailView.as_view()
)

from django.urls import path
from .views import UserSearchView

urlpatterns = [
    # existing urls

    path(
        'search/users/',
        UserSearchView.as_view(),
        name='user-search'
    ),
]