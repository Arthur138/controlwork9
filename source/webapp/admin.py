from django.contrib import admin
from webapp.models import Category, Ads, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Ads)
admin.site.register(Comment)
