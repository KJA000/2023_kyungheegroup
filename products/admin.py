
# Register your models here.

from django.contrib import admin
from .models import Product, Comment

class MainContentAdmin(admin.ModelAdmin):
 list_display = ['title', 'content', 'pub_date']
 search_fields = ['title']
 
class CommentAdmin(admin.ModelAdmin):
 list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
 search_fields = ['author']

admin.site.register(Product,MainContentAdmin)

admin.site.register(Comment,CommentAdmin)