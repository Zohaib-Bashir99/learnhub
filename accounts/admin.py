from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    ordering = ['email']
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
            (None, {"fields": ("email", "password")}),
            (("Personal info"), {"fields": ("first_name", "last_name")}),
            (
                ("Permissions"),
                {
                    "fields": (
                        "is_active",
                        "is_staff",
                        "is_superuser",
                        "groups",
                        "user_permissions",
                    ),
                },
            ),
            (("Important dates"), {"fields": ("last_login", "date_joined")}),
        )
    add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": ("email", "password1", "password2"),
                },
            ),
        )

    