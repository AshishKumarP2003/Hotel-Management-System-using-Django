from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from Room.models import Room

# Create your views here.
def getRoomView(request):
    rooms = Room.objects.filter(hotel_id = request.user['hotel'])
    return render(request, 'room.html', {'active_page': "room-list", 'rooms': rooms, 'role': request.user['role']})

def getAddRoomView(request):
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        room_type = request.POST.get('room_type')
        price_per_night = request.POST.get('price_per_night')

        room = Room.objects.filter(room_number=room_number)

        if room.exists():
            messages.info(request, 'Room already exists')
            return render(request, 'room_add.html', {'active_page': "room-add", 'role': request.user['role']})

        new_room = Room.objects.create(room_number=room_number, room_type=room_type, price_per_night=price_per_night, hotel_id = request.user['hotel'])
        new_room.save()
        messages.success(request, 'Room Added Successfully')
        return redirect("/room/")
    return render(request, 'room_add.html', {'active_page': "room-add", 'role': request.user['role']})

def deleteRoom(request, id):
    print(id)
    try:
        deleting = Room.objects.get(id=id)
        print(deleting)
        if (deleting):
            print('deleteing')
            deleting.delete()
            return JsonResponse({'type': 'success'}, status=200)
    except Room.DoesNotExist:
        return JsonResponse({'type': 'error'}, status=404)
    return JsonResponse({'type': 'error'}, status=404)


def getUpdateRoomView(request, id):
    
    updating = Room.objects.get(id=id)
    print(updating)
    if (request.method == 'POST'):
        updating.set_room_number(request.POST.get('room_number'))
        updating.set_price_per_night(request.POST.get('price_per_night'))
        updating.set_room_type(request.POST.get('room_type'))
        updating.save()
        messages.success(request, 'Room Added Successfully')
        return redirect("/room/")
    return render(request, 'room_update.html', {'active_page': "room-list", "room": updating, 'role': request.user['role']})
