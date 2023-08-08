from django.contrib import admin

from .models import CustomUser

#admin.site.register(CustomUser)

class CustomUserAdmin(admin.ModelAdmin):
    list_display=('id', 'email', 'first_name', 'last_name', 'role', 'is_active')
    readonly_fields=["created_at", "updated_at"]


    fieldsets=[
        (
            "Info",
            {
                "fields": [("first_name", "last_name", "middle_name"), "email", "password"],
            },
        ),
        (
            "Permission",
            {
                "fields": ["role", ("is_active", "is_staff", "is_superuser")],
                
            },
        ),
        (
            "Date_info",
            {
                "fields": ["created_at", "updated_at"],
                
            },
        ),
    ]
    
    def save_model(self, request, obj, form, change):
        obj.set_password(obj.password)
        super().save_model(request, obj, form, change)
        
admin.site.register(CustomUser, CustomUserAdmin)