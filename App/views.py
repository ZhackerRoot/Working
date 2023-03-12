from django.shortcuts import render, redirect
from .forms import CustomForm
from .models import Custom



def login(request):
    form = CustomForm()
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = CustomForm()
    return render(request, 'log.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def members(request):
    tables = Custom.objects.all()
    return render(request, "members.html", {'tables': tables})

def about(request):
    return render(request, 'about.html')