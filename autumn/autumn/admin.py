from django.contrib import admin
from models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'author')

admin.site.register(Blog, BlogAdmin)

admin.site.register(Author)