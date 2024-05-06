from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from Guest.models import Guest

# Create your views here.
def getGuestView(request):
    guests = Guest.objects.filter(hotel_id = request.user['hotel'])
    return render(request, 'guest.html', {'active_page': "guest-list", 'guests': guests, 'role': request.user['role']})

def getAddGuestView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        guest = Guest.objects.filter(name=name)

        if guest.exists():   
            messages.info(request, 'Guest already exists')
            return render(request, 'guest_add.html', {'active_page': "guest-add", 'role': request.user['role']})

        new_guest = Guest.objects.create(name=name, email=email, phone_number=phone_number, hotel_id = request.user['hotel'])
        new_guest.save()
        messages.success(request, 'Guest Added Successfully')
        return redirect("/guest/")
    return render(request, 'guest_add.html', {'active_page': "guest-add", 'role': request.user['role']})

def deleteGuest(request, id):
    print(id)
    try:
        deleting = Guest.objects.get(id=id)
        print(deleting)
        if (deleting):
            print('deleteing')
            deleting.delete()
            return JsonResponse({'type': 'success'}, status=200)
    except Guest.DoesNotExist:
        return JsonResponse({'type': 'error'}, status=404)
    return JsonResponse({'type': 'error'}, status=404)


def getUpdateGuestView(request, id):
    updating = Guest.objects.get(id=id)
    print(updating)
    if (request.method == 'POST'):
        updating.set_name(request.POST.get('name'))
        updating.set_phone_number(request.POST.get('phone_number'))
        updating.set_email(request.POST.get('email'))
        updating.save()
        messages.success(request, 'Guest Added Successfully')
        return redirect("/guest/")
    return render(request, 'guest_update.html', {'active_page': "guest-list", "guest": updating, 'role': request.user['role']})
