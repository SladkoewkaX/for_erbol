from django.shortcuts import render 

def mess(request):
    return render(request, 'hello.html')