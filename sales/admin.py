from django.contrib import admin
from .models import Customer, Item, Order



class ItemAdmin(admin.ModelAdmin):
    list_display = ('book', 'quantity', 'total_price')
    readonly_fields = ('total_price',)  


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer')

admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)