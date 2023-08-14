#define URL route for index() view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleItemMenuView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
