from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

def signup(request):
    template_name = 'auth_app/signup.html'
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('SIGN UP successfully')
    context = {'form': form}
    return render(request, template_name, context)

def login_view(request):
    template_name = 'auth_app/login.html'
    if request.method == "POST":
        un = request.POST['un']
        pw = request.POST['pw']
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect('show_url')
        else:
            return HttpResponse('enter correct username and password')
    return render(request, template_name)


def logout_view(request):
    logout(request)
    return redirect('login_url')
@login_required(login_url='login_url')
def change_pass(request):
    template_name = 'auth_app/change.html'
    if request.method == "POST":
        old = request.POST['old']
        new = request.POST['new']
        user = request.user
        res = user.check_password(old)
        if res:
            user.set_password(new)
            user.save()
            return redirect('login_url')
    return render(request, template_name)


