from django.contrib import admin

from .models import Event, User


class UserAdmin(admin.ModelAdmin):
    exclude = ["password"]


admin.site.register(User, UserAdmin)
admin.site.register(Event)
