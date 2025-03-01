from django.contrib import admin
from crawler.models import AmazonProduct, BewakoofProduct


class AmazonProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "product_link")
    search_fields = ("name", "price", "product_link")
    list_filter = ("category",)


class BewakoofProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "product_link")
    search_fields = ("name", "price", "product_link")
    list_filter = ("category",)

admin.site.register(AmazonProduct, AmazonProductAdmin)
admin.site.register(BewakoofProduct, BewakoofProductAdmin)
