from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order

# Create your views here.

from django.shortcuts import render, redirect
from .models import Order

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phoneNumber')
        food_item = request.POST.get('orderItem')
        quantity = int(request.POST.get('quantity'))
        total_price = calculate_total_price(food_item, quantity)  # Implement this function

        # Create and save the order
        Order.objects.create(
            name=name,
            phone_number=phone_number,
            food_item=food_item,
            quantity=quantity,
            total_price=total_price
        )

        return redirect('orders_table')  # Redirect to the same page after successful submission
    
    return render(request, 'restro/index.html')

def calculate_total_price(food_item, quantity):
    # Implement this function to calculate total price based on food item and quantity
    # You can define your own logic here
    prices = {
        '10': 10,
        '8': 8,
        '12': 12,
        '15': 15,
        '6': 6,
    }
    return prices.get(food_item, 0) * quantity


from .models import Order

def orders_table(request):
    orders = Order.objects.all()
    return render(request, 'Restro/view.html', {'orders': orders})

# Restro/views.py




# Restro/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order



def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('orders_table')

    return render(request, 'Restro/delete_confirm.html', {'order': order})

