from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework import generics

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    
    from rest_framework import generics
from .models import User

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    
    def get_queryset(self):
        query = self.request.GET.get('query', '')

        return User.objects.filter(
            username__icontains=query
        )
        
        from .serializers import RegisterSerializer, ProfileSerializer