from django.contrib import admin

from .models import Setting, Field, Instance, Value


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'active',)


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'setting', 'public', 'active',)
    list_filter = ('setting__name',)


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'setting', 'active',)
    list_filter = ('setting__name',)


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('value', 'field', 'instance', )
    list_filter = ('instance__setting__name', 'instance__name', 'field__name',)