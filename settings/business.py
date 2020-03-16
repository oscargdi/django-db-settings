from cachetools import TTLCache, cached
from django.conf import settings
from django.db import connection

from .models import Value

maxsize = settings.SETTINGS_CACHE_MAXSIZE if hasattr(
    settings, 'SETTINGS_CACHE_MAXSIZE') else 100
ttl = settings.SETTINGS_CACHE_TTL if hasattr(
    settings, 'SETTINGS_CACHE_TTL') else 60*60
settings_cache = TTLCache(maxsize, ttl)


@cached(settings_cache)
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
        settings_cache.clear()
        return True
    except:
        return False


def _dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def return_all_values():
    with connection.cursor() as cursor:
        cursor.execute("""select s.name s_name, i.name i_name, f.name f_name, f.public f_public, v.value v_value 
                        from settings_value v
                        INNER JOIN settings_field f on f.id = v.field_id
                        INNER JOIN settings_instance i on i.id = v.instance_id
                        INNER JOIN settings_setting s on s.id = i.setting_id""")
        return _dictfetchall(cursor)
