from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sessions.models import Session
from django.db.models import Sum
from django.db import connection
from django.shortcuts import redirect, render
from Booking.models import Booking
from Hotel.models import Hotel
from User.models import User
from django.http import JsonResponse
import jwt
import json
import calendar
from django.contrib import messages

# Create your views here.


# Dashboard View
def index(request):
    if request.method == "GET":
        if request.user["role"] == "super-admin":

            total_accounts = 0
            total_hotels = 0

            cursor = connection.cursor()
            
            # Get the Total Guest, Menus, Rooms and Available Rooms in Hotel
            if cursor.execute("""select "Hotels" as name, count(*) as counts from hotels union select "Accounts" as name, count(*) as counts from users where role="admin" """):
                record = cursor.fetchall()
                # print(record)
                if (len(record) == 2):
                    total_hotels = record[0][1]
                    total_accounts = record[1][1]

            return render(
                request,
                "super_admin_dashboard.html",
                {
                    "name": request.user["name"],
                    "role": request.user["role"],
                    "username": request.user["name"][0:8],
                    "page_data": {
                        "total_accounts": total_accounts,
                        "total_hotels": total_hotels,
                    }
                },
            )
        elif request.user["role"] == "admin":

            # Get the current month and year
            current_month = datetime.now().month
            current_year = datetime.now().year
            month = datetime.now().strftime("%B")
            total_guest = 0
            total_menu = 0
            total_room = 0
            total_available_room = 0
            booking_data={}
            revenue_data={}
            years = []
            annual_revenue_data={}

            # --------- Fetching Hotel Bookings and Revenue Stats ---------

            # Get the count of bookings for the current month
            booking_count_current_month = Booking.objects.filter(
                check_in_time__month=current_month,
                check_in_time__year=current_year,
                hotel_id_id=request.user['hotel']['id']
            ).count()

            # Get the count of bookings for the current year
            booking_count_current_year = Booking.objects.filter(
                check_in_time__year=current_year,
                hotel_id_id=request.user['hotel']['id']
            ).count()

            # Get the total amount generated for bookings in the current month
            total_amount_current_month = Booking.objects.filter(
                check_in_time__month=current_month,
                check_in_time__year=current_year,
                hotel_id_id=request.user['hotel']['id']
            ).aggregate(total_amount=Sum('amount'))['total_amount'] or 0

            # Get the total amount generated for bookings in the current year
            total_amount_current_year = Booking.objects.filter(
                check_in_time__year=current_year,
                hotel_id_id=request.user['hotel']['id']
            ).aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        
            
            # --------- Fetch Hotel Stats ---------
            
            cursor = connection.cursor()
            print(" abcd " , str(request.user['hotel']['id']))

            # Get the Total Guest, Menus, Rooms and Available Rooms in Hotel
            if cursor.execute("""SELECT "Guest" as name, COUNT(*) AS COUNT FROM guest where hotel_id_id=""" + str(request.user['hotel']['id']) + """ union SELECT "Available Room" as name, COUNT(*) AS COUNT FROM room where hotel_id_id=""" + str(request.user['hotel']['id']) + """ and reserved=0 union SELECT "Room" as name, COUNT(*) AS COUNT FROM room where hotel_id_id=""" + str(request.user['hotel']['id']) + """ union SELECT "Menu" as name, COUNT(*) AS COUNT FROM menu where hotel_id_id=""" + str(request.user['hotel']['id']) + """ """):
                record = cursor.fetchall()
                print("Records", record)
                if (len(record) == 4):
                    total_guest = record[0][1]
                    total_menu = record[3][1]
                    total_room = record[1][1]
                    total_available_room = record[2][1]
            
            # Get the Month vs Booking chart data
            if cursor.execute("""SELECT YEAR(check_in_time), MONTH(check_in_time) AS month, COUNT(*) AS count FROM booking where hotel_id_id=""" + str(request.user['hotel']['id']) + """ GROUP BY YEAR(check_in_time), MONTH(check_in_time) ORDER BY YEAR(check_in_time), MONTH(check_in_time)"""):
                data = cursor.fetchall()
                for row in data:
                    y = row[0]
                    year = "year_"+str(row[0])
                    month_num = row[1]
                    count = row[2]
                    # If year encounter for the first time, create year key with empty dict value to store months and values
                    if (year not in booking_data):
                        years.append(y)
                        booking_data[year] = {"months": [], "values": []}

                    # Get month name from month number
                    month_name = calendar.month_name[month_num][0:3]
                    if month_name not in booking_data[year]["months"]:
                        booking_data[year]["months"].append(month_name)
                        booking_data[year]["values"].append(count)

            # Get the Month vs Booking chart data
            if cursor.execute("""SELECT YEAR(check_in_time), MONTH(check_in_time) AS month, SUM(amount) AS count FROM booking where hotel_id_id=""" + str(request.user['hotel']['id']) + """ GROUP BY YEAR(check_in_time), MONTH(check_in_time) ORDER BY YEAR(check_in_time), MONTH(check_in_time)"""):
                data = cursor.fetchall()
                for row in data:
                    year = "year_"+str(row[0])
                    annual_year = "Year "+str(row[0])
                    month_num = row[1]
                    count = row[2]
                    # If year encounter for the first time, create year key with empty dict value to store months and values
                    if (year not in revenue_data):
                        annual_revenue_data[annual_year] = 0.0
                        revenue_data[year] = {"months": [], "values": []}

                    # Get month name from month number
                    month_name = calendar.month_name[month_num][0:3]
                    annual_revenue_data[annual_year] += float(count)

                    if month_name not in revenue_data[year]["months"]:
                        revenue_data[year]["months"].append(month_name)
                        revenue_data[year]["values"].append(int(count))
            # print(type(revenue_data['year_2020']['values'][0]))
            # print("\t\t\t\t", annual_revenue_data)
            # Render the dashboard
            return render(
                request,
                "admin_dashboard.html",
                {
                    "name": request.user["name"],
                    "role": request.user["role"],
                    "username": request.user["name"][0:8],
                    "page_data": {
                        "month": month,
                        "year": current_year,
                        "current_month_bookings": booking_count_current_month,
                        "current_year_bookings": booking_count_current_year,
                        "current_month_revenue": total_amount_current_month,
                        "current_year_revenue": total_amount_current_year,
                        "total_room": total_room,
                        "total_guest": total_guest,
                        "total_menu": total_menu,
                        "total_available_room": total_available_room,
                        "booking_data": booking_data,
                        "revenue_data": revenue_data,
                        "annual_revenue_data": annual_revenue_data,
                        "years": years
                    }
                },
            )
    return redirect("/")



# Login View
def login(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = User.objects.get(email=email)
            # print(email, password)
            # print(check_password(password, user.password))
            if check_password(password, user.password):
                jwt_object = {
                    "user_id": user.id,
                    "exp": datetime.now() + timedelta(days=1),
                }
                token = jwt.encode(jwt_object, settings.SECRET_KEY, algorithm="HS256")
                user.access_token = token
                user.save()
                request.session.create()
                request.session["user_id"] = user.id
                request.session["token"] = token

                request.session.set_expiry(0)
                messages.success(request, "Login Successful")
                return redirect("/dashboard/")
            else:
                messages.error(request, "Invalid Password")

        except User.DoesNotExist:
            messages.info(request, "User doesn't exists")
        except Exception as e:
            messages.error(request, e)

    return render(request, "login.html")


def profile(request):
    if request.method == "POST":
        # print(request.POST)
        user = User.objects.get(id=request.user["id"])
        user.name = request.POST.get("name")
        if request.user["role"] == "admin":
            hotel = Hotel.objects.get(id=request.user["hotel"]["id"])
            hotel.name = request.POST.get("hotel_name")
            hotel.phone_number = request.POST.get("phone_number")
            hotel.address = request.POST.get("address")
            hotel.save()
        user.save()
        return redirect("/profile/")
    if request.user:
        # print(request.user)
        return render(
            request,
            "profile.html",
            {
                "active_page": "profile",
                "name": request.user["name"],
                "role": request.user["role"],
                "username": request.user["name"][0:8],
                "user": request.user,
            },
        )
    return redirect("/")


def change_password(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=request.user['id'])
            print(user)
            body = json.loads(request.body)
            if user and check_password(body['old_password'], user.password):
                user.set_password(body['new_password'])
                user.save()
                return JsonResponse({'type': 'success', 'message': "Password Changed!"}, status=200)
            else:
                return JsonResponse({'type': 'error', 'message': "Incorrect Password!"}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'type': 'error', 'message': "User Not Found!!!"}, status=500)

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
    return redirect("/")  # Redirect to the login page after logout


# def guest(request):
#     return render(request, 'guest.html')
