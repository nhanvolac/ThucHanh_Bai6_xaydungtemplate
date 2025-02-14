from django.contrib import admin
from orders.models import Order, OrderItem
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address','postal_code','city', 'created','updateted', 'paid']
    list_filter = ['paid', 'created','updateted']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)