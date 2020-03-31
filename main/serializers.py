from rest_framework import serializers
from main.models import *
from datetime import datetime

class UserSerializer(serializers.Serializer):
    userid = serializers.IntegerField()
    username = serializers.CharField(max_length=100)
    mobileno = serializers.IntegerField()
    password = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=100)

    class Meta:
        model = user
        fields = ['userid', 'username', 'mobileno', 'password', 'gender']

    def validate_mobileno(self, mobileno):
        if user.objects.filter(mobileno=mobileno).count() != 0:
            return Response({"Failure": "Error"}, status=status.HTTP_400_BAD_REQUEST)
        return mobileno

    def create(self, validated_data, **kwargs):
        if user.objects.count() != 0:
            validated_data['userid'] = user.objects.last().userid + 1
        else:
            validated_data['userid'] = 1
        return user.objects.create(**validated_data)

class ItemSerializer(serializers.Serializer):
    itemid = serializers.IntegerField()
    itemname = serializers.CharField(max_length=100,required=False)
    itemimage = serializers.ImageField()
    maxprice = serializers.IntegerField()
    sellprice = serializers.IntegerField()
    itemdetail = serializers.CharField(max_length=200)

    class Meta:
        model = item
        fields = ['itemid', 'itemname', 'itemimage','maxprice', 'sellprice', 'itemdetail']

        def create(self, validated_data, **kwargs):
            if item.objects.count() != 0:
                validated_data['itemid'] = item.objects.last().itemid + 1
            else:
                validated_data['itemid'] = 1
            return item.objects.create(**validated_data)

class OrderSerializer(serializers.ModelSerializer):
    orderno = serializers.IntegerField()
    userid = serializers.IntegerField()
    orderamount = serializers.CharField(max_length=100)
    orderdate = serializers.CharField(max_length=100,required=False)
    delstatus = serializers.CharField(max_length=100, required=False)
    deltime = serializers.CharField(max_length=100, required=False)
    deladdress = serializers.CharField(max_length=200,required=False)

    class Meta:
        model = order
        fields = ['orderno', 'userid' , 'orderamount' , 'orderdate' , 'delstatus' , 'deltime' ,'deladdress']

    def create(self, validated_data, **kwargs):
        if order.objects.count() != 0:
            validated_data['orderno'] = order.objects.last().orderno + 1
        else:
            validated_data['orderno'] = 1

        validated_data['orderdate'] = datetime.now()
        return order.objects.create(**validated_data)

class OrderDetailSerializer(serializers.ModelSerializer):
    orderno = serializers.IntegerField()
    itemid = serializers.IntegerField()
    qty = serializers.IntegerField()
    amount = serializers.IntegerField()
    class Meta:
        model = orderdetail
        fields = ['orderno', 'itemid', 'qty', 'amount']
    def create(self, validated_data, **kwargs):
        return orderdetail.objects.create(**validated_data)


class DeliveryAddressSerializer(serializers.ModelSerializer):
    userid = serializers.IntegerField()
    orderno = serializers.IntegerField()
    delname = serializers.CharField(max_length=100)
    delstreet = serializers.CharField(max_length=100)
    delvillage = serializers.CharField(max_length=100)
    delcity = serializers.CharField(max_length=100)
    delzip = serializers.IntegerField()
    delphone = serializers.IntegerField()
    delnote = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = deliveryaddress
        fields = ['userid','orderno','delname','delstreet','delvillage','delcity','delzip','delphone','delnote']

class ItemUnitSerializer(serializers.ModelSerializer):
    itemid = serializers.IntegerField()
    unit = serializers.CharField(max_length=100)
    unit1 = serializers.CharField(max_length=100)
    unit2 = serializers.CharField(max_length=100,default="No Qty")
    unit3 = serializers.CharField(max_length=100,default="No Qty")
    unit4 = serializers.CharField(max_length=100,default="No Qty")
    unit5 = serializers.CharField(max_length=100,default="No Qty")
    unit6 = serializers.CharField(max_length=100,default="No Qty")
    unit7 = serializers.CharField(max_length=100,default="No Qty")
    unit8 = serializers.CharField(max_length=100,default="No Qty")
    unit9 = serializers.CharField(max_length=100,default="No Qty")
    unit10 = serializers.CharField(max_length=100,default="No Qty")

    class Meta:
        model = itemunit
        fields = ['itemid','unit','unit1','unit2','unit3','unit4','unit5','unit6','unit7','unit8','unit9','unit10']
