from django.contrib import admin
from .models import Post, Profile, Outgoing, Category, Look, Upload

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Outgoing)
admin.site.register(Category)
admin.site.register(Look)
admin.site.register(Upload)
