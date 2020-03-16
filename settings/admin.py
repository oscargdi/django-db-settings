from django.contrib import admin, messages
from django.shortcuts import redirect, render
from django.urls import path

from .business import clear_settings_cache
from .models import Field, Instance, Setting, Value


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'active',)
    search_fields = ('name',)


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

    change_list_template = 'settings/change_list_template.html'

    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.model_name
        urls = super().get_urls()
        my_urls = [
            path('refresh/', self.admin_site.admin_view(self.refresh_view),
                 name='%s_%s_refresh' % info),
            path('all/', self.admin_site.admin_view(self.all_view),
                 name='%s_%s_all' % info),
        ]
        return my_urls + urls

    def refresh_view(self, request):
        if clear_settings_cache():
            messages.add_message(request, messages.INFO,
                                 'Cache was successfully refreshed')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Cache could not be refreshed')
        return redirect('admin:settings_value_changelist')

    def all_view(self, request):
        context = {**self.admin_site.each_context(request), }
        return render(request, "settings/view_all_template.html", context)
