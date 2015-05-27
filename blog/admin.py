from django.contrib import admin
from blog.models import Category, Author, Article
from public.models import Tag

    
class ArticleAdmin(admin.ModelAdmin):

	def formfield_for_manytomany(self, db_field, request, **kwargs):
		if db_field.name == "tags":
			kwargs["queryset"] = Tag.objects.filter(use_range__in=[Tag.RANGE_ALL,Tag.RANGE_BLOG_ONLY])
		return super(ArticleAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

	class Media:
		js = (
            '/static/js/tiny_mce/tiny_mce_src.js', 
            '/static/js/tiny_mce/tiny_mce_config.js'
            )
        
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Article,ArticleAdmin)