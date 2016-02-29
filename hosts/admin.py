# -*- encoding:utf-8 -*-

# Register your models here.

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from hosts.models import MyUser
from hosts.customAdmin import UserAdmin

from hosts import models

admin.site.register(MyUser, UserAdmin)

class HostAdmin(admin.ModelAdmin):
    """
    主机表admin配置
    """
    list_display = ("host_name", "ip_addr", 'port', 'idc', "system_type", "enabled", "memo", "add_date")
    list_filter = ("idc", "system_type")
    search_fields = ("host_name", "ip_addr")
    list_editable = ("ip_addr","idc")
admin.site.register(models.Host, HostAdmin)

class IDCAdmin(admin.ModelAdmin):
    list_display = ("name", "memo")
admin.site.register(models.IDC, IDCAdmin)

class HostGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "memo")
admin.site.register(models.HostGroup, HostGroupAdmin)

class HostUserAdmin(admin.ModelAdmin):
    list_display = ("auth_type", "user_name", "password")
admin.site.register(models.HostUser, HostUserAdmin)

class BindHostToUserAdmin(admin.ModelAdmin):
    list_display = ("host", "host_user", "get_host_groups")
    filter_horizontal = ("host_groups",)
admin.site.register(models.BindHostToUser, BindHostToUserAdmin)

admin.site.register(models.TaskInfo)
admin.site.register(models.TaskLog)

admin.site.unregister(Group)