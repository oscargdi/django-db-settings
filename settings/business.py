from django.conf import settings

from .models import Value


def get_setting(setting, include_non_public=False):

    if include_non_public:
        values = Value.objects.filter(field__active=True, instance__active=True,
                                      instance__setting__active=True, instance__setting__name=setting)
    else:
        values = Value.objects.filter(field__active=True, field__public=True, instance__active=True,
                                      instance__setting__active=True, instance__setting__name=setting)

    result = {}

    for value in values:
        if not result.get(value.instance.name):
            result[value.instance.name] = {}
        result.get(value.instance.name)[value.field.name] = value.value

    return result


def clear_settings_cache():
    try:
        return True
    except:
        return False
