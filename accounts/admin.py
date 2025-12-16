from django.contrib import admin
from .models import CustomUser

admin.site.site_header = "Bookstore Admin"
admin.site.site_title = "Bookstore Admin Portal"
admin.site.index_title = "Welcome to Bookstore Admin Portal"
admin.site.register(CustomUser)
# Register your models here.
