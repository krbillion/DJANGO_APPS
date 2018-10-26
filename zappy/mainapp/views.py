from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'mainapp/index.html', context=None)

def signin(request):
    return render(request, 'registration/login.html', context)

# sign up user if they are not registered
def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = { "form" : form }
    return render(request, 'registration/signup.html', context)

def cart(request):
    context = { 'title': 'Cart'}
    return render(request, 'mainapp/cart.html', context)
