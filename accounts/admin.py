from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email',  'first_name', 'last_name', 'username', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def get_readonly_fields(self, request, obj=None):
        if obj:  # This ensures that the password is only read-only when editing an existing user
            return self.readonly_fields + ('password',)
        return self.readonly_fields

admin.site.register(Account, AccountAdmin)
