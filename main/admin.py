from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
admin.site.register(user)
admin.site.register(item)
admin.site.register(order)
admin.site.register(orderdetail)
