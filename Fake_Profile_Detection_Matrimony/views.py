from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup_form.html')


"""
def home(request):
    if request.session and request.session.__contains__('user_id'):
        return redirect('dashboard')
    return render(request, 'index.html')


def login(request):
    if request.session and request.session.__contains__('user_id'):
        return redirect('dashboard')
    return render(request, 'login.html')


def signup(request):
    if request.session and request.session.__contains__('user_id'):
        return redirect('dashboard')
    return render(request, 'signup.html')
"""
