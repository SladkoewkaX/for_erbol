from django.urls import path
from .views import mess, registr

urlpatterns = [
    path('', mess, name='message'),
    path('test/', registr, name='registr'),
]