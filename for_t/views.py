from django.http import request
from django.shortcuts import  render 
from .models import Registration
from .forms import RegistrationForm

def slovo(request):
    return render(request, 'hello.html')

def registration(request):
    form = RegistrationForm(request.POST or None)
    message = 'Заполните поля'
    if request.method == 'POST' and form.is_valid():
        message = 'Операция успешна выполнена'
        form.save()
        return render(request, 'button.html', {'form': form, 'message':message})
    return render(request, 'button.html', {'form': form, 'message':message})

def user_list(request):
    reg = Registration.objects.all()
    return render(request, 'spisok.html', {'reg':reg})

def detail(request,pk):
    details = Registration.objects.filter(pk=pk)
    return render (request,'details.html', {'details':details})
