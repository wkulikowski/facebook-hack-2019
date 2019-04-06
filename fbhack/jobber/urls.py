from django.urls import path

from .views import home, check_job, find_job

urlpatterns = [
    path('', home, name='jobber-home'),
    path('check', check_job, name='check'),
    path('find', find_job, name='find'),
]