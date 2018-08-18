from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import SignupForm

# def home(request):
#     return HttpResponse('Welcome to python world')

def home(request):
    template_name = 'home.html'
    return render(request, template_name)

def contact(request):
    template_name = 'contact.html'
    return render(request, template_name)


def signup(request):
    template_name = 'signup.html'
    if request.method  == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)
