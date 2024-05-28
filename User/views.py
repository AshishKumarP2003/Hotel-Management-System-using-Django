import datetime
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sessions.models import Session
from django.shortcuts import redirect, render
from Hotel.models import Hotel
from User.models import User
import jwt
from django.contrib import messages

# Create your views here.

# Dashboard View
def index(request):
    if (request.method == 'GET'):
        return render(request, 'index.html', {'name': request.user['name'], 'role': request.user['role'], 'username': request.user['name'][0:8]})
    return redirect('/')

# # Sign Up View
# def signup(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = User.objects.filter(email=email)

#         if user.exists():   
#             messages.info(request, 'User already exists')
#             return redirect('/')

#         new_user = User.objects.create(email=email)
#         new_user.set_password(password)
#         new_user.set_name(name)
#         new_user.save()
#         messages.success(request, 'Sign Up completed successfully')

        
#     return render(request, 'signup.html')

# Login View
def login(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.get(email=email)
            print(email, password)
            print(check_password(password, user.password))
            if check_password(password, user.password):
                jwt_object = {
                    'user_id': user.id,
                    'exp': datetime.datetime.now() + datetime.timedelta(days=1)
                }
                token = jwt.encode(jwt_object, settings.SECRET_KEY, algorithm = 'HS256')
                user.access_token = token
                user.save()
                request.session.create()
                request.session['user_id'] = user.id
                request.session['token'] = token

                request.session.set_expiry(0)
                messages.success(request, "Login Successful")
                return redirect('/dashboard/')
            else:
                messages.error(request, "Invalid Password")

        except User.DoesNotExist:
            messages.info(request, "User doesn't exists")
        except Exception as e:
            messages.error(request, e)

    return render(request, 'login.html')

def profile(request):
    if (request.method == "POST"):
        print(request.POST)
        user = User.objects.get(id = request.user['id'])
        user.name = request.POST.get('name')
        if (request.user['role'] == 'admin'):
            hotel = Hotel.objects.get(id = request.user['hotel']['id'])
            hotel.name = request.POST.get('hotel_name')
            hotel.phone_number = request.POST.get('phone_number')
            hotel.address = request.POST.get('address')
            hotel.save()
        user.save()
        return redirect('/profile/')
    if (request.user):
        print(request.user)
        return render(request, 'profile.html', {'active_page': "profile", 'name': request.user['name'], 'role': request.user['role'], 'username': request.user['name'][0:8], "user": request.user})
    return redirect('/')
        

# Logout View
def logout(request):
    try:
        # Flush the session to remove all session data
        request.session.flush()
        storage = messages.get_messages(request)
        storage.used = True
        messages.success(request, "Logout Successful")
    except Exception as e:
        messages.error(request, f"Error occurred during logout: {e}")
    return redirect('/')  # Redirect to the login page after logout

# def guest(request):
#     return render(request, 'guest.html')