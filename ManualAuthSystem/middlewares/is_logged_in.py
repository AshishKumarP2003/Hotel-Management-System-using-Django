from django.conf import settings
from django.http import JsonResponse
import jwt

from Hotel.models import Hotel, HotelAdmin
from User.models import User


class IsLoggedIn:
    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):
        # response = self.process_request(request)
        print("Islogged in called")
        user_id = request.session.get('user_id')
        token = request.session.get('token')
        print(token)
        if user_id and token:
            try:
                # Decode JWT token
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                if payload['user_id'] == user_id:
                    # Check if user exists in database
                    user = User.objects.get(id=user_id).__dict__
                    print(user['id'])
                    if user['role'] == 'admin':
                        hotel_id = HotelAdmin.objects.get(user_id=user['id']).__dict__['hotel_id_id']
                        hotel = Hotel.objects.get(id=hotel_id).__dict__
                        user['hotel'] = hotel
                    
                    del user['password']
                    del user['access_token']
                    print(user)

                    # # Update request with user object
                    request.user = user
                                        
                    # return None  # User authenticated, allow request to continue
                    return JsonResponse({'status': 'success', 'message': 'Logged in'}, status=200)
            except jwt.ExpiredSignatureError:
                return JsonResponse({'status': 'error', 'message': 'Token expired'}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({'status': 'error', 'message': 'Invalid token'}, status=401)
            except User.DoesNotExist:
                print('user not found')
                return JsonResponse({'status': 'error', 'message': 'User not found'}, status=404)
            except HotelAdmin.DoesNotExist:
                print('hotel admin not found')
                return JsonResponse({'status': 'error', 'message': 'User Hotel not found'}, status=401)
            except Hotel.DoesNotExist:
                print('hotel not found')
                return JsonResponse({'status': 'error', 'message': 'User Hotel not found'}, status=401)
        # If token doesn't exist or user not authenticated, return unauthorized
        return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=401)

