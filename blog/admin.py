from django.contrib import admin
from blog.models import Category, Author, Article

    
class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/tiny_mce/tiny_mce_src.js', 
            '/static/js/tiny_mce/tiny_mce_config.js'
            )
        
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Article,ArticleAdmin)