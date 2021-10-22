from django.urls import path
from .views import detail, registration, slovo, user_list

urlpatterns = [
    path('', slovo, name='message'),
    path('registration/', registration, name='registration'),
    path('spisok/', user_list , name='spisok'),
    path('spisok/<int:pk>/', detail , name='detail'),

]