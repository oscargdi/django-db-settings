from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import redirect

from .business import clear_settings_cache, get_setting


@staff_member_required
def get(request):
    return JsonResponse(get_setting(request.GET.get('setting')))


@staff_member_required
def refresh(request):
    return JsonResponse({'cache': {'result': clear_settings_cache()}})


@staff_member_required
def admin_refresh_page(request):
    if clear_settings_cache():
        messages.add_message(request, messages.INFO,
                             'Cache was successfully refreshed')
    else:
        messages.add_message(request, messages.ERROR,
                             'Cache could not be refreshed')
    return redirect('admin:settings_value_changelist')
