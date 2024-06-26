"""ManualAuthSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from User import urls as user_urls
# from Hotel import urls as hotel_urls
from User import views as user_views
from Hotel import views as hotel_views
from Guest import views as guest_views
from Menu import views as menu_views
from Room import views as room_views
from Booking import views as booking_views

urlpatterns = [
    # path('admin/', admin.site.urls),

    # User Basic Routes
    path('', user_views.login),
    path('logout/', user_views.logout),
    # path('signup/', user_views.signup),
    path('dashboard/', user_views.index),
    path('profile/', user_views.profile),
    path('change_password/', user_views.change_password),

    # Hotel Routes
    path('hotel/', hotel_views.Dashboard.as_view()),
    path('hotel/add/', hotel_views.getAddHotelView),
    path('hotel/<int:id>/edit/', hotel_views.getUpdateHotelView),
    path('hotel/<int:id>/delete/', hotel_views.deleteHotel),

    # Hotel Admins Manage Routes
    path('admin/', hotel_views.getAdminView),
    path('admin/add/', hotel_views.getAddAdminView),
    path('admin/<int:user_id>/reset/', hotel_views.getAdminResetPasswordView),
    path('admin/<int:id>/delete/', hotel_views.deleteHotelAdmin),

    # Manage Guests of a Hotel - Routes
    path('guest/', guest_views.getGuestView),
    path('guest/add/', guest_views.getAddGuestView),
    path('guest/<int:id>/delete/', guest_views.deleteGuest),
    path('guest/<int:id>/edit/', guest_views.getUpdateGuestView),

    # Manage menus of a Hotel - Routes
    path('menu/', menu_views.getMenuView),
    path('menu/add/', menu_views.getAddMenuView),
    path('menu/<int:id>/delete/', menu_views.deleteMenu),
    path('menu/<int:id>/edit/', menu_views.getUpdateMenuView),

    # Manage Rooms of a Hotel - Routes
    path('room/', room_views.getRoomView),
    path('room/add/', room_views.getAddRoomView),
    path('room/<int:id>/delete/', room_views.deleteRoom),
    path('room/<int:id>/edit/', room_views.getUpdateRoomView),

    # Manage Bookings in a Hotel - Routes
    path('booking/', booking_views.getBookingView),
    path('book/', booking_views.getBookView),
    path('room/<int:id>/book/', booking_views.getNewBookingView),
    path('booking/<int:id>/check-out/', booking_views.checkOut),
]
