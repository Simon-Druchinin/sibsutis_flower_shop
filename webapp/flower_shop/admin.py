from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import RangeNumericFilter, MultipleChoicesDropdownFilter, MultipleRelatedDropdownFilter, RangeDateFilter
from .models import Flower, Bouquet, BouquetFlower, Order


class BouquetFlowerInline(TabularInline):
    model = BouquetFlower
    extra = 1


@admin.register(Bouquet)
class BouquetAdmin(ModelAdmin):
    list_filter_submit = True
    list_fullwidth = True
    inlines = [BouquetFlowerInline]
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description')
    list_filter = (('price', RangeNumericFilter),)


@admin.register(Flower)
class FlowerAdmin(ModelAdmin):
    list_filter_submit = True
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description')
    list_filter = (('price', RangeNumericFilter),)


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_filter_submit = True
    list_display = ('user__username', 'user__email', 'order_date', 'bouquet', 'total_price')
    search_fields = ('user__username', 'user__email', 'bouquet__name')
    list_filter = (('order_date', RangeDateFilter), ('bouquet', MultipleRelatedDropdownFilter), ('total_price', RangeNumericFilter))
