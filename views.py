from django.shortcuts import render, redirect

from .models import Post
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout

from account import models
# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')
            elif user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def patient(request):
    context = {
        'posts': Post.objects.all
    }
    return render(request, 'patient.html', context)
    #return render(request,'patient.html')


def doctor(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.POST.get('image')
        category = request.POST.get('category')
        summary = request.POST.get('summary')
        content = request.POST.get('content')
    return render(request,'doctor.html')

def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Post(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/home')
    
    return render(request, 'newpost.html')


def myPost(request):
    context = {
        'posts': Post.objects.all
    }
    return render(request, 'mypost.html', context)


def signout(request):
    logout(request)
    return redirect('/login')