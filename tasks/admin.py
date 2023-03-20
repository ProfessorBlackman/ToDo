from django.contrib import admin

# Register your models here.
from .models import TasksData

admin.site.register((TasksData))