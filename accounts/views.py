from django.shortcuts import render,redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = UserLoginForm(request)

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')