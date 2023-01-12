from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TwitterForm
from . import models
# Create your views here.
def index(request):
     return render(request, 'scrapper/index.html')

def facebook(request):
     return render(request, 'scrapper/facebook.html')

def twitter(request):
    if request.method =='POST':
        form = TwitterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse('sonic:index'))
    else:
        form = TwitterForm()
    return render(request, 'scrapper/twitter.html',context={'form':form})

def reddit(request):
     return render(request, 'scrapper/reddit.html')

def data_analytics(request):
     return render(request, 'scrapper/data_analysis.html')
    

def add(request):
     if request.POST:
          username = request.POST['username']
          message_time = request.POST['message_time']
          message = request.POST['message']
          models.Message.objects.create(username=username,message_time=message_time,message=message)
          return redirect(reverse('sonic:lists'))
     else:
          return render(request, 'scrapper/add.html')

def delete(request):
     if request.POST:
          pk = request.POST['pk']
          try:
               models.Message.objects.get(pk=pk).delete()
               return redirect(reverse('sonic:lists'))
          except:
               print('pk not found!')
               return redirect(reverse('sonic:lists'))
     return render(request, 'scrapper/delete.html')

def lists(request):
     all_messages = models.Message.objects.all()
     context = {'all_messages':all_messages}
     return render(request, 'scrapper/lists.html', context = context)