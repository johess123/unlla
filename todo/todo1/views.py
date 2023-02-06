from django.shortcuts import render
from .models import alluser, alljob
from .forms import registForm, loginForm

# Create your views here.
def main(request):
    context = {
        'text': 'hello',
    }
    return render(request,'main.html',context)

def regist(request):
    form = registForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('name')
        user_list = alluser.objects.filter(name=name)
        if len(user_list) != 0:
            form = registForm()
            context = {
                'form': form,
                'alert1': True,
            }
            return render(request, 'regist.html',context)
        form.save()
        form = registForm()
        context = {
            'form': form,
            'doagain': False,
        }
        return render(request, 'regist.html', context)
    context = {
        'form': form,
    }
    return render(request, "regist.html", context)

def login(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('name')
        password = request.POST.get('password')
        user_list = alluser.objects.filter(name=name)
        if len(user_list) == 0:
            form = loginForm()
            context = {
                'form': form,
                'alert1': True,
            }
            return render(request, 'login.html',context)
        user_list = alluser.objects.filter(name=name,password=password)
        if len(user_list) == 0:
            form = loginForm()
            context = {
                'form': form,
                'alert2': True,
            }
            return render(request, 'login.html',context)
        request.session["user"] = name
        form = loginForm()
        context = {
            'form': form,
            'doagain': False,
        }
        return render(request, 'login.html', context)
    context = {
        'form': form,
    }
    return render(request, "login.html", context)