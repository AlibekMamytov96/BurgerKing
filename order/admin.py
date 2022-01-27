from django.contrib import admin

from .models import OrderItem, Order


class OrderItemInLine(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInLine]
    list_filter = ['created', ]
    list_display = ['id', 'address', 'created']
