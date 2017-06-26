from django.contrib import admin
from django.contrib.auth.models import User
from .models import File
# Register your models here.
class FileAdmin(admin.ModelAdmin):
    model = File
    fields = ['title', 'file', ]

admin.site.register(File, FileAdmin)
