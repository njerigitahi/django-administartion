from django.contrib import admin

from .models import (
    Service,
    Room,
    Asset,
    WorkFlow,
    Driver,
    Visitor,
    Supplier,
    Buyer,
    Season,
    Drop,
    Product,
    Order,
    Delivery
)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Season)
admin.site.register(WorkFlow)
admin.site.register(Visitor)
admin.site.register(Driver)
admin.site.register(Drop)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Asset)
admin.site.register(Room)
admin.site.register(Service)
admin.site.register(Delivery)
