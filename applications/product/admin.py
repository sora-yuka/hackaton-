from django.contrib import admin
from applications.file.models import File
from applications.order.models import Order
from .models import (
    Product, Category, Comment, Rating, Like, Favorite
)

class FileAdmin(admin.TabularInline):
    model = File
    fields = ('image',)
    max_num = 10

class PostAdmin(admin.ModelAdmin):
    inlines = [
        FileAdmin
    ]
    list_display = ['id', 'title', 'product_count_like']
    
    def post_count_like(self, obj):
        return obj.likes.filter(like=True).count()

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Like)
admin.site.register(Favorite)
admin.site.register(Order)