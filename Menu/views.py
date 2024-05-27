from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from Menu.models import Menu

# List of Menu of a Hotel - View
def getMenuView(request):
    menus = Menu.objects.filter(hotel_id = request.user['hotel'])
    return render(request, 'menu.html', {'active_page': "menu-list", 'menus': menus, 'role': request.user['role']})

# Add Menu to a Hotel
def getAddMenuView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')

        menu = Menu.objects.filter(name=name)

        if menu.exists():
            messages.info(request, 'Menu already exists')
            return render(request, 'menu_add.html', {'active_page': "menu-add", 'role': request.user['role']})

        new_menu = Menu.objects.create(name=name, price=price, description=description, hotel_id = request.user['hotel'])
        new_menu.save()
        messages.success(request, 'Menu Added Successfully')
        return redirect("/menu/")
    return render(request, 'menu_add.html', {'active_page': "menu-add", 'role': request.user['role']})

# Update Menu Information - View
def getUpdateMenuView(request, id):
    updating = Menu.objects.get(id=id)
    print(updating)
    if (request.method == 'POST'):
        updating.set_name(request.POST.get('name'))
        updating.set_description(request.POST.get('description'))
        updating.set_price(request.POST.get('price'))
        updating.save()
        messages.success(request, 'Menu Added Successfully')
        return redirect("/menu/")
    return render(request, 'menu_update.html', {'active_page': "menu-list", "menu": updating, 'role': request.user['role']})

# Delete Menu from Hotel Menu list - View
def deleteMenu(request, id):
    print(id)
    try:
        deleting = Menu.objects.get(id=id)
        print(deleting)
        if (deleting):
            print('deleteing')
            deleting.delete()
            return JsonResponse({'type': 'success'}, status=200)
    except Menu.DoesNotExist:
        return JsonResponse({'type': 'error'}, status=404)
    return JsonResponse({'type': 'error'}, status=404)
