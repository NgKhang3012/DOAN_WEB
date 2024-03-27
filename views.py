from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('username')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('home')
        else: 
            form = CustomUserCreationForm()
            return render(request, 'signup.html', {'form': form})
            