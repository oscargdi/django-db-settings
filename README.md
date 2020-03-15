# django-db-settings

django-db-settings is a Django app to save your configuration in cacheable DB objects that are easily defined like classes.

## Quick start


1. Install `django-db-settings` using `pip`:

```bash
    $ pip install django-db-settings
```

2. Add "settings" to your INSTALLED_APPS setting like this::

```python
    INSTALLED_APPS = [
        ...
        'settings',
    ]
```

3. Include the settings URLconf in your project urls.py like this::

```python
    path('settings/', include('settings.urls')),
```

4. Run `python manage.py migrate` to create the settings models.

5. Start the development server and visit http://127.0.0.1:8000/admin/ to setup your app settings (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/settings/?setting=YOUR_SETTING to get the objects related to that specific setting (JSON).

7. Find the REFRESH SETTINGS button with in Value model change list page. This project uses TTL based cache, which can be configured by adding the following setting:

    - SETTINGS_CACHE_MAXSIZE: To set the maximum size of total items in the cache. By default set to 100.
    - SETTINGS_CACHE_TTL: To set the Time To Live of the cache items. By default set to 3600 seconds (1 hour).


## Basic Usage

django-db-settings saves your settings in a flexible model. To create a setting follow these steps:

1. Create a setting in model `Setting`, it will act like the class that will group a set of settings. e.g., `product type`

2. Define the attributes of this `Setting` by adding them in model `Field`. You can set each as public or private. e.g., `title`, `description`, `code`.

3. Add `Setting` instances in model `Instance`. They will act as the objects of the setting class. e.g., `saving`, `credit card`, `loan`.

4. Finally, add values in model `Value` for every instance guided by the fields defined for `Setting`. e.g., for `saving` instance, values are `title`: Saving account, `description`: Saves you money, `code`: S001.

After adding all values, you will be able to retrieve all those which fields are public by going to http://127.0.0.1:8000/settings/?setting=product%20type. It returns a JSON object:

```json
{"saving": {"title": "Saving account", "description": "Save your money with us!"}, "credit card": {"title": "Credit Card", "description": "Get the best from our Credit Card"}, "loan": {"title": "Loan", "description": "We loan you the money you need"}}
```

TIP: You can use the same settings internally by calling method `get_setting` in module `settings.business`:

```python
>>> from settings.business import get_setting
>>> get_setting('product type')
{'saving': {'title': 'Saving account', 'description': 'Save your money with us!'}, 'credit card': {'title': 'Credit Card', 'description': 'Get the best from our Credit Card'}, 'loan': {'title': 'Loan', 'description': 'We loan you the money you need'}}
```

Internally, you can set parameter `include_non_public=True` to retrieve private fields also:

```python
>>> get_setting('product type', include_non_public=True)
{'saving': {'title': 'Saving account', 'description': 'Save your money with us!', 'code': 'S-001'}, 'credit card': {'title': 'Credit Card', 'code': 'C-001', 'description': 'Get the best from our Credit Card'}, 'loan': {'title': 'Loan', 'description': 'We loan you the money you need', 'code': 'L-001'}}
```

Call method `clear_settings_cache` from the same package to clear the cache and refresh the global settings.

```python
>>> from settings.business import clear_settings_cache
>>> clear_settings_cache()
True
```