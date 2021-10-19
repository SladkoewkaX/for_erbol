from django.shortcuts import render 

from .forms import RegForm

def mess(request):
    return render(request, 'hello.html')

def registr(request):
    form = RegForm(request.POST or None)
    message = 'Заполните поля'
    if request.method == 'POST' and form.is_valid():
        message = 'Операция успешна выполнена'
        form.save()
        return render(request, 'hello.html', {'form': form, 'message':message})
    return render(request, 'hello.html', {'form': form, 'message':message})