from django.contrib import admin

from commerce.models import Brand, PcSpec, Product, ProductType

admin.site.register(Brand)
admin.site.register(PcSpec)
admin.site.register(Product)
admin.site.register(ProductType)
