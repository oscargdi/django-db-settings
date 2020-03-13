from django.urls import path

from . import views

urlpatterns = [
    path('', views.get),
    path('refresh/', views.refresh, name='settings-refresh'),
]
