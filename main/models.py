from django.db import models

class user(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=100)
    mobileno = models.IntegerField()
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

class item(models.Model):
    itemid = models.IntegerField()
    itemname = models.CharField(max_length=100)
    itemimage = models.ImageField(upload_to='itemimages/')
    maxprice = models.IntegerField()
    sellprice = models.IntegerField()
    itemdetail = models.CharField(max_length=200)

class order(models.Model):
    orderno = models.IntegerField()
    userid = models.IntegerField()
    orderamount = models.CharField(max_length=100)
    orderdate = models.CharField(max_length=100)
    delstatus = models.CharField(max_length=100,null=True)
    deltime = models.CharField(max_length=100,null=True)
    deladdress = models.CharField(max_length=100,null=True)


class orderdetail(models.Model):
    orderno = models.IntegerField()
    itemid = models.IntegerField()
    itemname = models.CharField(max_length=100)
    qty = models.IntegerField()
    amount = models.IntegerField()

class deliveryaddress(models.Model):
    userid = models.IntegerField()
    orderno = models.IntegerField()
    delname = models.CharField(max_length=100)
    delstreet = models.CharField(max_length=100)
    delvillage = models.CharField(max_length=100)
    delcity = models.CharField(max_length=100)
    delzip = models.IntegerField()
    delphone = models.IntegerField()
    delnote = models.CharField(max_length=100,null=True)

class itemunit(models.Model):
    itemid = models.IntegerField()
    unit = models.CharField(max_length=100)
    unit1 = models.CharField(max_length=100,default="No Qty")
    unit2 = models.CharField(max_length=100,default="No Qty")
    unit3 = models.CharField(max_length=100,default="No Qty")
    unit4 = models.CharField(max_length=100,default="No Qty")
    unit5 = models.CharField(max_length=100,default="No Qty")
    unit6 = models.CharField(max_length=100,default="No Qty")
    unit7 = models.CharField(max_length=100,default="No Qty")
    unit8 = models.CharField(max_length=100,default="No Qty")
    unit9 = models.CharField(max_length=100,default="No Qty")
    unit10 = models.CharField(max_length=100,default="No Qty")




