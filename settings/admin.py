from django.contrib import admin

from .models import Field, Instance, Setting, Value


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'active',)
    search_fields = ('name',)

    change_list_template = 'settings/change_list_template.html'


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'setting', 'public', 'active',)
    list_filter = ('setting__name',)
    search_fields = ('setting__name', 'name',)


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'setting', 'active',)
    list_filter = ('setting__name',)
    search_fields = ('setting__name', 'name',)


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('value', 'field', 'instance', )
    list_filter = ('instance__setting__name', 'instance__name', 'field__name',)
    search_fields = ('instance__setting__name',
                     'instance__name', 'field__name',)
