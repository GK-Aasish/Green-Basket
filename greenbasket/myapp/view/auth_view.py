from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def signup_view(request):
    errors = {}
    if request.method == 'POST':
        fristname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        #form validation
        if not  fristname:
            errors['firstname'] = 'First name is required'
        if not lastname:
            errors['lastname'] = 'Last name is required'
        if not email:
            errors['email'] = 'Email is required'
        if not password:
            errors['password'] = 'Password is required'
        if password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match'

        if errors:
           return render(request, 'signup.html', {'errors': errors, 'data': request.POST})  
        else:
            if User.objects.filter(username=email).exists():
                errors['email'] = 'Email is already in use'
                return render(request, 'signup.html', {'errors': errors, 'data': request.POST})
            else:
                user = User.objects.create_user(username=email,email=email, password=password, first_name=fristname, last_name=lastname)
                messages.success(request, 'Account created successfully')
                return redirect('login')
    return render(request, 'signup.html',)

#return the data received in case of any error in the form submission using errors variable and display it in the template and return
def login_view(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #form validation
        if not username:
            errors['username'] = 'Username is required'
        if not password:
            errors['password'] = 'Password is required'
        if  not errors:
            user = User.objects.filter(username=username).first()
            if user is not None and user.check_password(password):
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('home')
            else:
                errors['general'] = 'Invalid username or password'
                return redirect('login',{'data':request.POST})
        
        else:
            return render(request, 'login.html', {'errors': errors, 'data': request.POST})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')