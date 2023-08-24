from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect("dash")
        
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username = username)
            
            if not user_obj.exists ():
                messages.info(request, "Account not Found")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            
            user_obj = authenticate(username = username, password = password)

            if user_obj and user_obj.is_superuser: 
                login(request, user_obj)
                return redirect("dash")
            
            messages.info(request, "Invalid Password!")
            return redirect('login')

        return render(request, 'login.html')
    
    except Exception as e:
        print(e)

def admin_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dash(request):
    return render(request, "dashboard.html")

@login_required(login_url='login')
def documentation(request):
    return render(request, "documentation.html")
