from django.contrib import admin

from tool.models import Tool

class ToolAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/tiny_mce/tiny_mce_src.js', 
            '/static/js/tiny_mce/tiny_mce_config.js'
            )

admin.site.register(Tool,ToolAdmin)