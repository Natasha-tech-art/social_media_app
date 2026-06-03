from rest_framework import generics

from .models import User
from .serializers import ProfileSerializer, RegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer


class UserSearchView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return User.objects.filter(username__icontains=query)
