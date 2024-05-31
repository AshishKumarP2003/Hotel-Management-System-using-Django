from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views import View

from Hotel.models import Hotel, HotelAdmin
from User.models import User

# View Dashboard
class Dashboard(View):
    def get(self, request):
        hotel = Hotel.objects.all()
        return render(request, 'hotel.html', {'hotels': hotel, 'active_page': "hotel-list", 'role': request.user['role']})
    

# ================================= Hotel ===================================

# View Hotels
def getHotelView(request):
    return render(request, 'hotel.html', {'active_page': "hotel-list"})

# Remove Hotel
def deleteHotel(request, id):
    print(id)
    deleting = Hotel.objects.get(id=id)
    print(deleting)
    if (deleting ):
        print('deleting')
        deleting.delete()
        # deleting.save()
        return JsonResponse({'type': 'success'}, status=200)
    return JsonResponse({'type': 'error'}, status=404)

# Update Hotel
def getUpdateHotelView(request, id):
    updating = Hotel.objects.get(id=id)
    print(updating)
    if (request.method == 'POST'):
        print('deleeing')
        updating.set_name(request.POST.get('name'))
        updating.set_phone_number(request.POST.get('phone_number'))
        updating.set_address(request.POST.get('address'))
        updating.save()
        # deleting.save()
        messages.success(request, 'Hotel Added Successfully')
        return redirect("/hotel/")
    return render(request, 'hotel_update.html', {'active_page': "hotel-list", "hotel": updating, 'role': request.user['role']})

# Add Hotel
def getAddHotelView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        hotel = Hotel.objects.filter(name=name)

        if hotel.exists():   
            messages.info(request, 'Hotel already exists')
            return render(request, 'hotel_add.html', {'active_page': "hotel-add", 'role': request.user['role']})

        new_hotel = Hotel.objects.create(name=name, address=address, phone_number=phone_number)
        new_hotel.save()
        messages.success(request, 'Hotel Added Successfully')
        return redirect("/hotel/")
    return render(request, 'hotel_add.html', {'active_page': "hotel-add", 'role': request.user['role']})



# ====================== Hotel Admin =============================

# View Hotel Admins
def getAdminView(request):
    try:
        data = HotelAdmin.objects.select_related('user_id', 'hotel_id').values('id', 'user_id__id', 'user_id__name', 'user_id__email', 'hotel_id__name')
        return render(request, 'hotel_admin.html', {'active_page': "admin-list", 'role': request.user['role'], 'data': data})
    except Exception as e:
        messages.info(request, 'Email already exists')
        return render(request, 'hotel_admin.html', {'active_page': "admin-list", 'role': request.user['role'], 'data': {}})


# Add Hotel Admin
def getAddAdminView(request):
    hotels = Hotel.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hotel_id = int(request.POST.get('hotel_id'))
        print(request.POST)

        user = User.objects.filter(email=email)
        print(user)
        if user.exists():
            print("user exists")
            messages.info(request, 'Email already exists')
            return render(request, 'hotel_admin_add.html', {'active_page': "admin-add", 'hotels': hotels, 'role': request.user['role']})

        new_user = User.objects.create(name=name, email=email, password=make_password(password), role="admin")
        new_user.save()
        print(new_user)

        hotel = Hotel.objects.filter(id = hotel_id)
        if not hotel.exists():
            messages.info(request, "Hotel Doesn't exists")
            return render(request, 'hotel_admin_add.html', {'active_page': "admin-add", 'hotels': hotels, 'role': request.user['role']})
        print(hotel)
        hotel_admin = HotelAdmin.objects.create(hotel_id=hotel[0], user_id=new_user)
        hotel_admin.save()
        messages.success(request, 'Hotel Added Successfully')
        return redirect("/admin/")


    return render(request, 'hotel_admin_add.html', {'active_page': "admin-add", 'hotels': hotels, 'role': request.user['role']})

# Reset Password
def getAdminResetPasswordView(request, user_id):

    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_password')
        if (password != confirm_pass):
            messages.error(request, "Password Doesn't Match")
            try:
                user = User.objects.filter(id=user_id)
                print(user)
                if user.exists():
                    return render(request, 'hotel_admin_reset_password.html', {'active_page':'admin-list', 'user': user[0], 'role': request.user['role']})
            except User.DoesNotExist:
                messages.error(request, "User does not exist")
                print("user not found")
                return redirect("/admin/")
        user_update = User.objects.get(id=user_id)
        user_update.set_password(password)
        user_update.save()
        messages.success(request, "Password updated successfully")
        print("success")
        return redirect("/admin/")

    try:
        user = User.objects.filter(id=user_id)
        print(user)
        if user.exists():
            return render(request, 'hotel_admin_reset_password.html', {'active_page':'admin-list', 'user': user[0], 'role': request.user['role']})
    except User.DoesNotExist:
        messages.error(request, "User does not exist")
        return redirect("/admin/")
    return redirect("/admin/")


# Remove Hotel Admin
def deleteHotelAdmin(request, id):
    print(id)
    try:
        deleting = HotelAdmin.objects.get(id=id)
        print(deleting)
        if (deleting):
            user_id = deleting.user_id
            deleting.delete()
            user = User.objects.get(id=user_id.id)
            if (user):
                user.delete()
                print('Deleted Successfully')
                return JsonResponse({'type': 'success'}, status=200)
            else:
                return JsonResponse({'type': 'error'}, status=404)
        else:
            return JsonResponse({"type": "error"}, status=404)
    except HotelAdmin.DoesNotExist:
        return JsonResponse({"type": "error"}, status=404)
    except HotelAdmin.MultipleObjectsReturned:
        return JsonResponse({"type": "error"}, status=404)
    except User.DoesNotExist:
        return JsonResponse({"type": "error"}, status=404)
    except User.MultipleObjectsReturned:
        return JsonResponse({"type": "error"}, status=404)
