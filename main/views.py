from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main.models import *
from main.serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.shortcuts import render, get_object_or_404
import requests
import httplib2
import urllib
import nexmo
class UserList(generics.ListCreateAPIView):
    queryset=user.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = user.objects.all()
        u = self.request.query_params.get('u',None)
        if u is not None:
            queryset = queryset.filter(mobileno=u)
            return queryset
        return queryset

class ItemList(generics.ListCreateAPIView):
    queryset=item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = item.objects.all()
        il = self.request.query_params.get('il', None)
        if il is not None:
            queryset = queryset.filter(itemname=il)
            return queryset
        return queryset

class OrderList(generics.ListCreateAPIView):
    queryset=order.objects.all()
    serializer_class = OrderSerializer
    def get_queryset(self):
        queryset = order.objects.all()
        o = self.request.query_params.get('o',None)
        u = self.request.query_params.get('u', None)
        if u is not None:
            queryset = queryset.filter(userid=u)
            return queryset
        if o is not None:
            queryset = queryset.filter(orderid=o)
            return queryset
        return queryset

class OrderDetailList(generics.ListCreateAPIView):
    queryset=orderdetail.objects.all()
    serializer_class = OrderDetailSerializer
    def get_queryset(self):
        queryset = orderdetail.objects.all()
        o = self.request.query_params.get('o',None)
        if o is not None:
            queryset = queryset.filter(orderid=o)
            return queryset
        return queryset

class DeliveryAddressList(generics.ListCreateAPIView):
    queryset=deliveryaddress.objects.all()
    serializer_class = DeliveryAddressSerializer
    def get_queryset(self):
        queryset = deliveryaddress.objects.all().values()
        u = self.request.query_params.get('u', None)
        if u is not None:
            queryset=deliveryaddress.objects.filter(userid=u).all()
        return queryset

class ItemUnitList(generics.ListCreateAPIView):
    model = itemunit
    serializer_class = ItemUnitSerializer;
    def get_queryset(self):
        queryset = itemunit.objects.all().values()
        i = self.request.query_params.get('i', None)
        if i is not None:
            queryset=itemunit.objects.filter(itemid=i).all()
        return queryset



def order_intialise(request):
    order1 = order.objects.last()
    data = {
        "order": order1.orderno,
        "deliverycharge" : "10"
    }
    return JsonResponse(data)

def user_auth(request,pk):
    order1 = user.objects.filter(mobileno=pk)
    http = httplib2.Http()
    body = {'sender_id':'FSTSMS','message':'This is a test message','language':'english','route':'p','numbers':'8059976498'}
    data = {'otp': 'success'}

    client = nexmo.Client(key='af753d55', secret='De9Ls0AvAZvKInzw')

    client.send_message({
        'from': 'Vonage SMS API',
        'to': '918059976498',
        'text': 'Hello from Vonage',
    })

    return JsonResponse({'status':'false','message':"User Already Exists"}, status=500)
