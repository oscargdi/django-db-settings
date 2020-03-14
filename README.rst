=====
django-db-settings
=====

django-db-settings is a Django app to save your configuration in cacheable DB objects that are easily defined like classes.

Quick start
-----------

1. Add "settings" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'settings',
    ]

2. Include the settings URLconf in your project urls.py like this::

    path('settings/', include('settings.urls')),

3. Run ``python manage.py migrate`` to create the settings models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ to setup your app settings (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/settings/?setting=YOUR_SETTING to get the objects related to that specific setting (JSON).

6. Find the REFRESH SETTINGS button with in Value model change list page. This project uses TTL based cache, which can be configured by adding the following setting:

    - SETTINGS_CACHE_MAXSIZE: To set the maximum size of total items in the cache. By default set to 100.
    - SETTINGS_CACHE_TTL: To set the Time To Live of the cache items. By default set to 3600 seconds (1 hour).