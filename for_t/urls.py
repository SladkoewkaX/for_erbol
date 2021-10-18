from django.urls import path
from .views import mess

urlpatterns = [
    path('', mess, name='message'),
]