from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.filter(user=user)
    if profile: 
        profile = Profile.objects.get(user=user)

    return render(request, 'index.html', {"profile":profile})


def signup_main(request):
    return render(request, 'signup_main.html')


def signup_check(request):
    if not request.POST.get('chk_1', None) == None:
        if not request.POST.get('chk_2', None) == None:
            return redirect('accounts_signup')
        else:
            return render(request, 'signup_main.html')
    else:
        return render(request, 'signup_main.html')
    


def signup_infor(request):
    return render(request, 'signup_infor.html')


def signup_fin(request):
    return render(request, 'signup_fin.html')


def accounts_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        print(form.errors)
        if form.is_valid():
            user = form.save()
            user.save()
            auth_login(request, user)
            Profile.objects.create(user=user)
            return redirect("feed:feedList")
        else:
            ctx = {
                "form": form,
            }
            return render(request, "accounts_signup.html", ctx)

    elif request.method == "GET":
        form = SignUpForm()
        ctx = {
            "form": form,
        }
        return render(request, "accounts_signup.html", ctx)


def accounts_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        email = request.POST.get("email")
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect("feed:feedList")
        else:
            ctx = {
                "form": form,
                "error": "email or password is incorrect",
            }
            return render(request, "accounts_login.html", ctx)
    elif request.method == "GET":
        form = LoginForm()
        ctx = {
            "form": form,
        }
        return render(request, "accounts_login.html", ctx)


def accounts_logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("feed:feedList")
    elif request.method == "GET":
        auth_logout(request)
        # return render(request, "feedhome.html")
        return redirect("feed:feedList")


def accounts_home(request):
    return render(request, "accounts_home.html")


def signup_success(request):
    return render(request, "signup_success.html")


def login_success(request):
    return render(request, "login_success.html")


def logout_success(request):
    return render(request, "logout_success.html")


def create_introduction(request):
    if request.method == 'POST':
        if request.FILES.get('image'):
            Introduction.objects.create(
                title = request.POST['title'],
                body = request.POST['body'],
                image = request.POST['image']
            )
        else:
            Introduction.objects.create(
                title = request.POST['title'],
                body = request.POST['body']
            )
        Intro = Introduction.objects.all()
        return render(request, 'create_intrduction.html', {'Intro':Intro})
    return redirect('/')