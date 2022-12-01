from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm##ProfileForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        ##f1 = ProfileForm(request.POST)
        if form.is_valid(): ##and f1.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            print(profile.user)
            profile.save()
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
        ##f1 = ProfileForm()
    return render(request, 'users/register.html', {'form':form}) ##'f1':f1})

def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')


