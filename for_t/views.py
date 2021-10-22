from django.shortcuts import get_object_or_404, render 
from .models import Registration
from .forms import RegForm

def mess(request):
    return render(request, 'hello.html')

def registr(request):
    form = RegForm(request.POST or None)
    message = 'Заполните поля'
    if request.method == 'POST' and form.is_valid():
        message = 'Операция успешна выполнена'
        form.save()
        return render(request, 'button.html', {'form': form, 'message':message})
    return render(request, 'button.html', {'form': form, 'message':message})

def spisok(request):
    reg = Registration.objects.all()
    return render(request, 'spisok.html', {'reg':reg})

def get_list(request, pk):
    details = Registration.objects.filter(pk=pk)
    return render(request, 'details.html', {'details':details})
