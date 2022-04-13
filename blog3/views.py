from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
from blog3.forms import SignUpForm


def signup(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('blog1:home')
            else:
                messages.error(request=request, message="Invalid username or password.", extra_tags='p',
                               fail_silently=False)
        else:
            messages.error(request=request, message="Invalid username or password", extra_tags='p', fail_silently=False)
    form = AuthenticationForm()

    return render(request=request, template_name='blog3/signup.html', context={'signup': form})


def registration(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('blog3:registration')

    else:
        form = SignUpForm()

    return render(request, 'blog3/registration.html', {'registration': form})
