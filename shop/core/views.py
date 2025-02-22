from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
def main(request):
    return render(request, 'core/main.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['Email']
        r_password = request.POST['repeat_password']
        if  password != r_password:
            return render(request, 'core/auth/signup.html', {'error': 'пароль не сходиться'})
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('signin')
    return render(request, 'core/auth/signup.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'core/auth/signin.html',{'error':'не верный логин или пароль'})
    return render(request, 'core/auth/signin.html')
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'core/auth/profile.html')
    else:
        return redirect('signin')

def signout(request):
    logout(request)
    return redirect('signin')


