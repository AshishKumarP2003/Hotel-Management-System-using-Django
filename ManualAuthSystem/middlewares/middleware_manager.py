from django.shortcuts import redirect
from ManualAuthSystem.middlewares.config import CUSTOM_MIDDLEWARES, MIDDLEWARE_MAPPINGS
from django.urls import get_resolver, resolve

class MiddlewareManager:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        middleware_list = MIDDLEWARE_MAPPINGS.get(get_resolver().resolve(request.path).route, [])
        for middle_name in middleware_list:
            if middle_name in CUSTOM_MIDDLEWARES:
                print(CUSTOM_MIDDLEWARES[middle_name].__name__)
                middleware_instance = CUSTOM_MIDDLEWARES[middle_name](self.get_response)
                response = middleware_instance(request)
                print(response)
                if (type(response).__name__ == 'JsonResponse'):
                    
                    if (response.status_code and response.status_code != 200):
                        if (response.status_code == 401):
                            return redirect('/')
                        return response

        return self.get_response(request)

