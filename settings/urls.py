from django.urls import path

from . import views

urlpatterns = [
    path('', views.get),
    path('refresh/', views.refresh, name='settings-refresh'),
    path('admin/refresh/', views.admin_refresh_page,
         name='settings-refresh-admin'),
]
