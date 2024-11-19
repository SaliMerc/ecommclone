from django.contrib import admin
from morningDjangoHtmlFormsProject.models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'qtty', 'size', 'price')
admin.site.register(Product,ProductAdmin)