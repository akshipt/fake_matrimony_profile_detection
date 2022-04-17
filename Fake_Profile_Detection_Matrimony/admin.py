from django.contrib import admin
from .models import AdminPanel  # , PersonalInfo


# Register your models here.

class UserAdminModel(admin.ModelAdmin):
    model = AdminPanel


# admin.site.register(PersonalInfo)
admin.site.register(AdminPanel, UserAdminModel)
