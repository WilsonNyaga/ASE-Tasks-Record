from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib import admin
from .models import Client, Task, Comment, Attachment  # Import your models

# Register your models here

admin.site.register(Client)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Attachment)
