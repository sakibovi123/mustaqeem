from django.shortcuts import render
from Cart.cart import *

# Create your views here.


def cart_details(request):
    cart = Cart(request)
   
    productString = ""
    
    for item in cart:

        
        product = item['product']
        
        if product.sale_price:
            b = "{'id':'%s','title':'%s','sale_price':'%s','quantity':'%s', 'total_price':'%s'},"%(product.id, product.title, product.sale_price, item['quantity'], item['total_price'])
        
            productString = productString + b
        else:
             b = "{'id':'%s','title':'%s','market_price':'%s','quantity':'%s', 'total_price':'%s'},"%(product.id, product.title, product.market_price, item['quantity'], item['total_price'])

             productString = productString + b
    context = {
        'cart': cart,
        'productString': productString,
        
    }
    
    return render(request, 'cart.html', context)