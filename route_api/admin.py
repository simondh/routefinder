from django.contrib import admin


# Register your models here.
from route_api.models import Routes

class RouteAdmin(admin.ModelAdmin):
    fields = ('node_a', 'node_b')

admin.site.register(Routes, RouteAdmin)