from django.urls import path
from .views import get_list, mess, registr, spisok

urlpatterns = [
    path('', mess, name='message'),
    path('test/', registr, name='registr'),
    path('spisok/', spisok , name='spisok'),
    path('spisok/<int:pk>/', get_list , name='get_list'),

]