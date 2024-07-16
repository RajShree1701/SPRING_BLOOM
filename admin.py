from django.contrib import admin
from django.utils.html import format_html
from . models import Product,Category,Order
# Register your models here.
from . models import Flowershop

@admin.register(Flowershop)
class FlowershopAdmin(admin.ModelAdmin):
    list_display = ('admin_id', 'admin_name','admin_price')

#class CategoryAdmin(admin.ModelAdmin)
#    list_display=('cat_id','cat_name')
admin.site.register(Category)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def prdImg(self,obj):
        return format_html('<img src="{}" width="50" height="50"/>'.format(obj.image.url))
    list_display=('name','description','price','prdImg','category','product_info','delivery_charge','delivery_info')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('user', 'address', 'product', 'quantity', 'payment_status')