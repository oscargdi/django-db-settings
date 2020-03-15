from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import redirect

from .business import clear_settings_cache, get_setting


@staff_member_required
def get(request):
    return JsonResponse(get_setting(request.GET.get('setting')))
