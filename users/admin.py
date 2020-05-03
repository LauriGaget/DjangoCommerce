from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import UserCustom


class CustomUserAdmin(UserAdmin):
    # add_form =
    # form =
    model = UserCustom
    list_display = ["username", "email", "is_staff"]


admin.site.register(UserCustom, CustomUserAdmin)