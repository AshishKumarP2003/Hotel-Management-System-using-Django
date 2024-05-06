
from django.http import JsonResponse

from Hotel.models import Hotel, HotelAdmin


class SetHotelInfo:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user:
            return JsonResponse({'type': 'error', 'message': 'Invalid User'}, status=401)
        else:
            print(request.user['id'])
            admin = HotelAdmin.objects.filter(user_id = request.user['id'])
            if admin:
                hotel = Hotel.objects.get(id=admin[0].hotel_id.id)
                print(hotel)
                request.user['hotel'] = hotel
                return JsonResponse({'type': 'success', 'message': 'Super Admin'}, status=200)
        return JsonResponse({'type': 'error', 'message': 'Forbidden'}, status=403)