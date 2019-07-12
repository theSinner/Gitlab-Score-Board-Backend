from django.contrib import admin
from .models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
                    "id",
                    "username",
                    "full_name",
                    "created_at",
                ]
