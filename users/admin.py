from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):


    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
    (
        "Custom Profile",
        {
            "fields": (
                "avatar",
                "company",
                "nickname"
            )
        },
    ),
    )

    list_display = ("username", "email", "company", "email_verified", "login_method")
    list_display_links = ("username", "email", "company")
    list_filter = ("username", "email", "company")