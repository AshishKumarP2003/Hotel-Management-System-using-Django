
from typing import Any

from django.http import JsonResponse

from Hotel.models import Hotel, HotelAdmin


class IsValidAdminOrSuper:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user:
            return JsonResponse({'type': 'error', 'message': 'Invalid User'}, status=401)
        else:
            print(request.user['role'])
            if (request.user['role'] == 'admin'):
                print("Role is admin")
                try:
                    admin_of_hotel = HotelAdmin.objects.get(user_id=request.user['id'])
                    if admin_of_hotel:
                        hotel = Hotel.objects.get(id=admin_of_hotel.hotel_id.id)
                        if (hotel):
                            request.user['is_validated'] = True
                            return JsonResponse({'type': 'success', 'message': 'Super Admin'}, status=200)
                        else:
                            return JsonResponse({'type': 'error', 'message': 'Hotel Not Found'}, status=404)
                    else:
                        pass
                except HotelAdmin.DoesNotExist as e:
                    return JsonResponse({'type': 'error', 'message': e}, status=403)
                return JsonResponse({'type': 'error', 'message': 'Unauthorized'}, status=401)
            elif request.user['role'] == 'super-admin':
                print("User is Super Admin")
                return JsonResponse({'type': 'success', 'message': 'Super Admin'}, status=200)
        return JsonResponse({'type': 'error', 'message': 'Forbidden'}, status=403)