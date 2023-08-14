from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Menu
from ..serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Set up test instances of Menu
        Menu.objects.create(name="Dish 1", description="Delicious dish", price=9.99)
        Menu.objects.create(name="Dish 2", description="Another dish", price=12.99)
        
        self.client = APIClient()  # Initialize the test client

    def test_getall(self):
        # Retrieve all Menu objects using the API
        url = reverse('menu-list')  # Assuming you've named the viewset's URL 'menu-list'
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)  # Serialize all instances

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)