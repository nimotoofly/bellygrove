# yourappname/urls.py
from django.urls import path
from .views import index, details, success_page

urlpatterns = [
    path('', index, name='index'),
    path('details/', details, name='details'),
    path('success/', success_page , name='success_page'),
]
