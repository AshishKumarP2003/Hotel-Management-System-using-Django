from ManualAuthSystem.middlewares.is_valid_admin import IsValidAdmin
from .is_logged_in import IsLoggedIn
from .is_valid_super import IsValidSuper
from .is_valid_admin_or_super import IsValidAdminOrSuper
from .set_hotel_info import SetHotelInfo

CUSTOM_MIDDLEWARES = {
    'IsLoggedIn': IsLoggedIn,
    'IsValidAdmin': IsValidAdmin,
    'IsValidSuper': IsValidSuper,
    'IsValidAdminOrSuper': IsValidAdminOrSuper,
    'SetHotelInfo': SetHotelInfo
}

MIDDLEWARE_MAPPINGS = {
    'dashboard/': ['IsLoggedIn', 'IsValidAdminOrSuper'],
    'hotel/': ['IsLoggedIn', 'IsValidSuper'],
    'hotel/add/': ['IsLoggedIn', 'IsValidSuper'],
    'admin/': ['IsLoggedIn', 'IsValidSuper'],
    'admin/add/': ['IsLoggedIn', 'IsValidSuper'],
    'admin/<int:user_id>/reset/': ['IsLoggedIn', 'IsValidSuper'],
    #asdad
    'guest/': ['IsLoggedIn', 'IsValidAdmin', 'SetHotelInfo'],
    'guest/add/': ['IsLoggedIn', 'IsValidAdmin', 'SetHotelInfo'],
    'guest/<int:id>/edit/': ['IsLoggedIn', 'IsValidAdmin', 'SetHotelInfo'],

    'menu/': ['IsLoggedIn', 'IsValidAdmin', 'SetHotelInfo'],
    'menu/add/': ['IsLoggedIn', 'IsValidAdmin', 'SetHotelInfo'],
    'menu/<int:id>/edit/': ['IsLoggedIn', 'IsValidAdmin', 'SetHotelInfo'],

    'room/': ['IsLoggedIn', 'IsValidAdmin', 'SetHotelInfo'],
    'room/add/': ['IsLoggedIn', 'IsValidAdmin', 'SetHotelInfo'],
    'room/<int:id>/edit/': ['IsLoggedIn', 'IsValidAdmin', 'SetHotelInfo'],

    'booking/': ['IsLoggedIn', 'IsValidAdmin', 'SetHotelInfo'],
    'book/': ['IsLoggedIn', 'IsValidAdmin', 'SetHotelInfo'],
    'room/<int:id>/book/': ['IsLoggedIn', 'IsValidAdmin', 'SetHotelInfo'],
}