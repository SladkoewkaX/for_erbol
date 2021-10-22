from django.http import request
from django.shortcuts import redirect, render 
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

def spisok(request):
    reg = Registration.objects.all()
    return render(request, 'spisok.html', {'reg':reg})

def get_detail(request,pk):
    details = Registration.objects.filter(pk=pk)
    # if request.method == 'GET':
    #     return redirect('details.html', {'details':details})
    return render (request,'details.html', {'details':details})
