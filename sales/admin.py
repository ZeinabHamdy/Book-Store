from django.contrib import admin
from .models import Customer, Item, Order



class ItemAdmin(admin.ModelAdmin):
    list_display = ('book', 'customer_username', 'quantity','total_price',)
    readonly_fields = ('total_price',)  

    def customer_username(self,obj):
        return obj.order.customer.username



class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','customer','total_price',)
    readonly_fields = ('total_price',)  

    def order_id(self, obj):
        return f"Order #{obj.id}"


admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)