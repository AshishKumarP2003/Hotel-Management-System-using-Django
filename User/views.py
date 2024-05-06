import datetime
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sessions.models import Session
from django.shortcuts import redirect, render
from User.models import User
import jwt
from django.contrib import messages

# Create your views here.

def index(request):
    if (request.method == 'GET'):
        print(request.user)
        return render(request, 'index.html', {'name': request.user['name'], 'role': request.user['role']})
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email)

        if user.exists():   
            messages.info(request, 'User already exists')
            return redirect('/')

        new_user = User.objects.create(email=email)
        new_user.set_password(make_password(password))
        new_user.set_name(name)
        new_user.save()
        messages.success(request, 'Sign Up completed successfully')

        
    return render(request, 'signup.html')

def login(request):

    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.get(email=email)

            if check_password(password, user.password):
                jwt_object = {
                    'user_id': user.id,
                    'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=1)
                }
                token = jwt.encode(jwt_object, settings.SECRET_KEY, algorithm = 'HS256')
                user.access_token = token
                user.save()
                request.session.create()
                request.session['user_id'] = user.id
                request.session['token'] = token

                request.session.set_expiry(0)
                messages.success(request, "Login Successful")
            else:
                messages.error(request, "Invalid Password")

        except User.DoesNotExist:
            messages.info(request, "User doesn't exists")
        except Exception as e:
            messages.error(request, e)

    return render(request, 'login.html')

def logout(request):
    try:
        # Flush the session to remove all session data
        request.session.flush()
        messages.success(request, "Logout Successful")
    except Exception as e:
        messages.error(request, f"Error occurred during logout: {e}")
    return redirect('/')  # Redirect to the login page after logout

# def guest(request):
#     return render(request, 'guest.html')