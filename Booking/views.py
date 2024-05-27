import datetime
from django.utils import timezone
import json
from django.shortcuts import render
from django.db import IntegrityError

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from Booking.models import Booking
from Guest.models import Guest
from Room.models import Room

# Booking List - View
def getBookingView(request):
    booking = Booking.objects.filter(hotel_id = request.user['hotel'])
    return render(request, 'booking.html', {'active_page': "booking-list", 'bookings': booking, 'role': request.user['role']})

# Get New Booking - View
def getBookView(request):
    rooms = Room.objects.filter(hotel_id = request.user['hotel'])
    return render(request, 'book.html', {'active_page': "book", "rooms": rooms, 'role': request.user['role']})

# Add New Booking Record - View
def getNewBookingView(request, id):

    # Check if the room is vacant or not.
    if request.method == 'POST':
        room = Room.objects.filter(id=id)
        if (room):
            if (room[0].reserved == False):
                return JsonResponse({"type": 'success', 'message': "Room is Vacant"}, status=200)
            else:
                return JsonResponse({"type": 'error', 'message': "Try booking some other Room...", 'title': "Room is Occupied"}, status=409)
        else:
            return JsonResponse({"type": 'error', 'message': "The Room you are trying to book doesn't exists", "title": "Room not Found"}, status=404)
    
    # Show the Booking Template with Room and guest list to select from.
    if request.method == 'GET':
        guests = Guest.objects.filter(hotel_id=request.user['hotel'])
        room = Room.objects.filter(id=id)
        return render(request, 'book_room.html', {'active_page': "book", 'room': room[0], 'guests': guests, 'role': request.user['role']})
    
    # Handle New Booking
    if request.method == 'PUT':
        guest_id = int(json.loads(request.body)['guest_id'])
        guest = Guest.objects.filter(id=guest_id)
        room = Room.objects.filter(id=id)
        if (room):
            # Check if the room is reserved or not.
            if (room[0].reserved == False):
                booking = Booking.objects.filter(room_id=id, check_out_time=None)
                # Double Check: if Someone booked but room reserved status didn't change.
                if (booking):
                    return JsonResponse({"type": 'error', 'message': "The Room you are trying to book is Occupied", "title": "Room is Occupied"}, status=409)
                else:
                    # Book the Room 
                    book = Booking.objects.create(room_id=room[0], guest_id=guest[0], hotel_id=request.user['hotel'], check_in_time=datetime.datetime.now())
                    if (book):
                        try:
                            # Update the Room Status.
                            room_update = Room.objects.get(id=id)
                            room_update.reserved = True
                            room_update.save()
                            return JsonResponse({"type": 'success', "message": "Room has been Booked successfully", "title": "Room Booked"}, status=200)
                        except Exception as e:
                            return JsonResponse({"type": 'error', 'message': "Something Went Wrong!!!", "title": "Server Error"}, status=409)
                    else:
                        return JsonResponse({"type": 'error', 'message': "Something Went Wrong!!!", "title": "Server Error"}, status=409)
            else:
                booking = Booking.objects.filter(guest_id=guest_id, room_id=id, check_out_time="")
                if (booking):
                    return JsonResponse({"type": 'error', 'message': "The Room is already booked for "+booking[0].guest_id__name, "title": "Room already booked"}, status=409)
                else:
                    return JsonResponse({"type": 'error', 'message': "The Room you are trying to book is Occupied", "title": "Room is Occupied"}, status=409)
        else:
            return JsonResponse({"type": 'error', 'message': "The Room you are trying to book doesn't exists", "title": "Room not Found"}, status=404)
 


# Check out from Hotel - View
def checkOut(request, id):
    booking = Booking.objects.filter(id=id)

    # Check if record exists and did he already checked out?
    if (booking == None):
        return JsonResponse({"type": 'error', 'message': "There is no such booking record found", "title": "Booking not Found"}, status=404)
    elif (booking[0].check_out_time != None):
        return JsonResponse({"type": 'error', 'message': "Guest has already checked out", "title": "Already Checked Out"}, status=404)
    else:
        # If Not, Update the Booking Check out time, generate amount and vacant room.
        try:
            # Updating the Amount and Checkout time.
            update = Booking.objects.get(id=id)
            print(booking[0].check_in_time)
            print(type(booking[0].check_in_time))
            check_in_time = booking[0].check_in_time
            check_out_time = timezone.now()
            total_hours = (check_out_time - check_in_time).total_seconds() / (60 * 60)
            amount = (total_hours / 24) * booking[0].room_id.price_per_night
            print("Total Time Spent => ", total_hours)
            print(timezone.now() , datetime.datetime.now(), timezone.now() == datetime.datetime.now())
            update.check_out_time = datetime.datetime.now()
            update.amount = round(amount, 2)
            update.save()

            # Updating the Room Status to vacant.
            room = Room.objects.get(id=booking[0].room_id.id)
            room.reserved = False
            room.save()
            return JsonResponse({"type": 'success', 'message': "Checked Out Successfully", "title": "Checked Out", "hour": round(total_hours, 2), "amount": amount}, status=500)
        
        except IntegrityError as e:
            # Handle integrity errors (e.g., unique constraint violation)
            print(f"IntegrityError occurred: {e}")
            return JsonResponse({"type": 'error', 'message': "Something Went Wrong", "title": "Server Error"}, status=500)


        except Exception as e:
            # Handle other exceptions
            print(f"An error occurred: {e}")
            return JsonResponse({"type": 'error', 'message': "Something Went Wrong", "title": "Server Error"}, status=500)
