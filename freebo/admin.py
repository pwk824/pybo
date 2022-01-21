from django.contrib import admin
from .models import Freewriting

class FreewritingAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Freewriting,FreewritingAdmin)


