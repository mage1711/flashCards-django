from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
from .backends import EmailBackend
from .models import FlashCard
from django.contrib.auth.decorators import  login_required
from .forms import CreateAccountForm
def index(request):
    flashcards = FlashCard.objects.filter(private=False)
    context ={'flashcards':flashcards}
    return render(request,'index.html',context)


@login_required(login_url='login')
def homePage(request):
    if request.method == 'POST':
        title = request.POST.get('frontText')
        content = request.POST.get('backText')
        subject = request.POST.get('subject')
        private = request.POST.get('private')
        if private:
            private = True
        else:
            private = False
        owner = request.user.email
        FlashCard.objects.create(title=title,content=content,subject=subject,private=private,owner=owner)
        return redirect('homePage')
    flashCards = FlashCard.objects.filter(owner= request.user.email)
    subjects = FlashCard.objects.values('subject').distinct()[:5]
    context = {'flashcards': flashCards,'subjects':subjects}
    return render(request, 'index.html', context)


def search(request):
    if request.method == 'GET':
        print(request.GET)
        flashcards = FlashCard.objects.filter(subject__contains=request.GET.get('search'))
        if flashcards:
            context = {'flashcards': flashcards}
            return render(request, 'index.html', context)
        else:
            messages.info(request, 'No results found')
            return redirect('index')

def signUp(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.user.is_authenticated:
        return redirect('index')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password1 = request.POST.get('password')
            password2 = request.POST.get('confirm_password')
            email = request.POST.get('email')
            usernameIsUnique = not (User.objects.filter(username=username).exists())
            emailIsUnique = not (User.objects.filter(email=email).exists())
            if password1 == password2 and usernameIsUnique and emailIsUnique:
                User.objects.create_user(username= username, email=email, password=password1).save()
                return redirect('index')
    context = {}
    return render(request,'signup.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request)
        user = EmailBackend().authenticate(request=request,username = username,password = password)
        # user = authenticate(request,username = username,password = password)
        if user is not None:
            auth_login(request, user)
            return redirect('homePage')
    context = {}
    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('index')