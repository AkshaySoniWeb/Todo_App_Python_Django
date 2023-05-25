from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import Form, LoginForm
from .models import UserTask
from django.db.models import Q

# Create your views here.


# This Projects created by AkshaySoni Python-Django Developer contact- 9098888977
# Signup
def Signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = SignUpForm()
            messages.success(
                request,
                "We're grateful that you've joined us. Thank you for signing up!",
            )
            return redirect("login")

    else:
        fm = SignUpForm()

    return render(request, "course/signup.html", {"form": fm})


# Login
def UserLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data["username"]
                upass = fm.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Congrats!! Now you are logged in..🙋🏻")
                    return redirect(
                        "profile"
                    )  # Redirect to the "profile" named URL pattern
        else:
            fm = LoginForm()
        return render(request, "course/login.html", {"form": fm})
    else:
        return redirect("profile")


# Add & Show
def Home(request):
    stud = UserTask.objects.all()
    if request.user.is_authenticated:
        data = request.GET.get("search")
        stud = UserTask.objects.all()

        if data:
            stud = stud.filter(
                Q(title__icontains=data) | Q(key__icontains=data) | Q(details__icontains=data)
            )

        if request.method == "POST":
            fm = Form(request.POST)
            if fm.is_valid():
                ti = fm.cleaned_data["title"]
                ke = fm.cleaned_data["key"]
                de = fm.cleaned_data["details"]
                ac = fm.cleaned_data["active"]
                sv = UserTask(title=ti, key=ke, details=de, active=ac)
                sv.save()
                fm = Form()

                messages.success(request, f"Congrats!! Your todo '{ti}' added..🙋🏻")
                return redirect("home")  # Assuming you have a URL pattern named 'home'
        else:
            fm = Form()

        return render(
            request,
            "course/addshow.html",
            {"form": fm, "st": stud, "name": request.user},
        )
    else:
        return redirect("login")


# Update
def update_data(request, id):
    if request.method == "POST":
        pi = UserTask.objects.get(pk=id)
        fm = Form(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Task Updated!!")
    else:
        pi = UserTask.objects.get(pk=id)
        fm = Form(instance=pi)
    return render(request, "course/update.html", {"form": fm})


# Delete
def DeleteData(request, id):
    if request.method == "POST":
        pi = UserTask.objects.get(pk=id)
        pi.delete()
        return redirect("home")


# Profile
def Profile(request):
    return render(request, "course/profile.html", {"name": request.user})


# logout
def UserLogout(request):
    logout(request)
    return redirect("login")
