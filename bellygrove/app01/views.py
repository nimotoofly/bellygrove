# yourappname/views.py
from django.shortcuts import render, redirect
from .models import UserInfo,Order
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        shopping_cart = data.get('shoppingCart', [])
        counts = data.get('counts', [])

        # Serialize shopping cart data
        serialized_cart = json.dumps([
            {'name': item['name'], 'price': item['price'], 'count': item['count']}
            for item, count in zip(shopping_cart, counts)
        ])

        # Save the serialized shopping cart data as a single object
        Order.objects.create(cart_data=serialized_cart)

        return JsonResponse({'message': 'Data saved successfully!'})
    return render(request, 'app01/index.html')

def details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        apartment = request.POST.get('apartment')
        roomNumber = request.POST.get('roomNumber')
        phoneNumber = request.POST.get('phoneNumber')

        # Save data to the database
        UserInfo.objects.create(
            name=name,
            apartment=apartment,
            roomNumber=roomNumber,
            phoneNumber=phoneNumber
        )

        return redirect('success_page')

    return render(request, 'app01/details.htm')
    
def success_page(request):
    return render(request, 'app01/success_page.html')
