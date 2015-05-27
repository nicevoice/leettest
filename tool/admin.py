from django.contrib import admin

from tool.models import Tool
from public.models import Tag

class ToolAdmin(admin.ModelAdmin):

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "tags":
            kwargs["queryset"] = Tag.objects.filter(use_range__in=[Tag.RANGE_ALL,Tag.RANGE_TOOL_ONLY])
        return super(ToolAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

	class Media:
		js = (
            '/static/js/tiny_mce/tiny_mce_src.js', 
            '/static/js/tiny_mce/tiny_mce_config.js'
            )

admin.site.register(Tool,ToolAdmin)