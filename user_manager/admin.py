from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.site_header = 'ELITE FIT CENTER'
admin.site.site_title =  'Elite Fit Center'
admin.site.index_title = 'Panel de administración'

class CustomUserAdmin(UserAdmin):

    list_display = ('email', 'full_name', 'is_active', 'is_staff')
    search_fields = ('email', 'full_name')
    readonly_fields = ('date_joined',)
    ordering = ['email'] 

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields':  ('full_name', 'identification_document', 'is_passport', 'gender', 'age', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions'),'classes': ('collapse',) }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'full_name', 'identification_document', 'is_passport', 'gender', 'age', 'phone_number', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
