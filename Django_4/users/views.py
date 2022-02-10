from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from .form import LoginForm, RegisterForm,DeleteForm

def login_wiew(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home:homepg')

    context={
        'form': form,
        'title': "Giriş Yap"
    }
    return render(request, 'login.html', context=context)

def register_view(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user=authenticate(username=user.username,password=password)
        login(request,new_user)
        return redirect('home:homepg')
    context={
            'form': form,
            'title': "Üye Ol"
        }
    return render(request, 'login.html', context=context)

def delete_view(request):
    form=DeleteForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password1')
        new_user=authenticate(username=user.username,password=password)
        if new_user:
            user.delete()
            user.save()
        logout(request)
        return redirect('post:logins')
    context={
        'form': form,
        'title': "Kullanıcı Sil"
    }
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('home:homepg')

