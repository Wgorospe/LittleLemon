from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def post(self, request):
        return render(request,'',{})
    
    def get(self,request):
        return render(request,'',{})
    

class SingleItemMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def post(self, request):
        return render(request,'', {})
    
    def put(self, request):
        return render(request,'',{})
    
    def delete(self, request):
        return render(request,'',{})
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 