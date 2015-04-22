from django.contrib import admin
from blog.models import Category, Author, Article


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Article)