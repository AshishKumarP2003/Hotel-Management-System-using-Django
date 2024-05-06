
from typing import Any

from django.http import JsonResponse

from Hotel.models import Hotel, HotelAdmin


class IsValidSuper:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user:
            return JsonResponse({'type': 'error', 'message': 'Invalid User'}, status=401)
        else:
            print(request.user['role'])
            if request.user['role'] == 'super-admin':
                print("User is Super Admin")
                return JsonResponse({'type': 'success', 'message': 'Super Admin'}, status=200)
        return JsonResponse({'type': 'error', 'message': 'Forbidden'}, status=403)