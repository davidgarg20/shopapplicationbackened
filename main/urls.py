from django.urls import path
from main import views
from main.views import *

urlpatterns = [
    path('user/', UserList.as_view()),
    path('order/', OrderList.as_view()),
    path('item/', ItemList.as_view()),
    path('orderdetail/', OrderDetailList.as_view()),
    path('orderd/', order_intialise),
    path('usera/<int:pk>/', user_auth),
    path('deliveryaddress/', DeliveryAddressList.as_view() ),
    path('itemunit/', ItemUnitList.as_view())
]