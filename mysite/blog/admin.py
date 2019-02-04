from django.contrib import admin
from .models import Blogpost, Keyword

# Register your models here.

admin.site.register(Blogpost)
admin.site.register(Keyword)