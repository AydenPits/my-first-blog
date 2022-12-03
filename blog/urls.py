from django.urls import path
from . import view

urlpatterns = [path('', view.post_list, name='post_list')]