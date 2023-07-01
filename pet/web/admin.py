from django.contrib import admin
from . models import Product,Order,OrderItem,fristemail,contact_data,leave_cont


# Register your models here.

class orderitemtube(admin.TabularInline):
    model=OrderItem

class orderadmin(admin.ModelAdmin):
   inlines=[orderitemtube]


admin.site.register(Product)

admin.site.register(Order,orderadmin)

admin.site.register(OrderItem)

admin.site.register(fristemail)

admin.site.register(contact_data)

admin.site.register(leave_cont)

