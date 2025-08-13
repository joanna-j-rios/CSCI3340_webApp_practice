from django.shortcuts import render, redirect
from .models import Record
from .forms import AddRecordForm


# Create your views here.

def home(request):
    records = Record.objects.all()
    #return render(request, 'home.html',{})
    return render(request, 'home.html', {'records':records})


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_record = form.save()
            return redirect('home')
    return render(request, 'add_record.html', {'forms':form})
