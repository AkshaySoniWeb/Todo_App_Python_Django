from django.contrib import admin

from .models import UserTask
from .forms import Form


# Register your models here.


@admin.register(UserTask)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "key", "details", "active"]
