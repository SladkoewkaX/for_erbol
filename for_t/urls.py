from django.urls import path
from .views import get_detail, registration, slovo, spisok

urlpatterns = [
    path('', slovo, name='message'),
    path('registration/', registration, name='registr'),
    path('spisok/', spisok , name='spisok'),
    path('spisok/<int:pk>/', get_detail , name='get_detail'),

]