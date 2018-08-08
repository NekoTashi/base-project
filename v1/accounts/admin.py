from django.contrib import admin

from v1.accounts.models.user import User


class UserAdmin(admin.ModelAdmin):
    exclude = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)
