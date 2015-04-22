from django.contrib import admin
from crowd.models import TestCycle,TestCase,TestBug


admin.site.register(TestCycle)
admin.site.register(TestCase)
admin.site.register(TestBug)