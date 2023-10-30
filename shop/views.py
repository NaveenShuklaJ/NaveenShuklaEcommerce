from math import ceil
import json
from django.shortcuts import render, redirect

from .models import OrderUpdate, Product, Orders
from django.contrib.auth.decorators import login_required
    

# Create your views here.

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def LoginPage(request):

    if request.method == "POST":
        uname = request.POST.get('usernamee')
        passwd = request.POST.get('passwordd')

        user =  User.objects.filter(username = uname)
        if user:
            u = authenticate(username =uname, password=passwd)

            if u is None:
                messages.error(request, "Wrong Password...")
                return redirect('/shop/login/')

            else:
                # print('Correct pass')
                login(request, u) 
                return redirect('/shop/')   
            
        else:
            messages.error(request, 'User does not exists with this username')
            redirect('/shop/login/')


    return render(request, 'shop/login.html')

def RegisterPage(request):

    
    if request.method == "POST":
        uname = request.POST.get('usernamee')
        mail = request.POST['emaill']
        passwd = request.POST.get('passwordd')
        

        checke =  User.objects.filter(username = uname)

        if checke.exists():
            # print("Username exists in views.py")
            messages.add_message(request, messages.ERROR, "Username already exists....")
            return redirect('/shop/register/')

        user = User.objects.create(
            username = uname,
            email = mail,
        )

        user.set_password(passwd)
        user.save()
        # print('data saved \n')
        messages.info(request, 'Account created successfully...')
        login(request, user)
        return redirect('/shop/')

    return render(request, 'shop/register.html')

def LogoutPage(request):
    logout(request)
    return redirect('/shop/login/')


@login_required(login_url="/shop/login/")
def ShowProductView(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # formula for defining the no. of slide windows in carousel according to the number of items per category
    # windows = n//4 + ceil((n/4)-(n//4))

    ProductData = []
    catprods = Product.objects.values('category')
    categoryWise = {item['category'] for item in catprods}
    for Differentcategory in categoryWise:
        prod = Product.objects.filter(category=Differentcategory)
        n = len(prod)
        # categoryWise defining the no. of slide
        windows = n // 4 + ceil((n / 4) - (n // 4))
        ProductData.append([prod, range(1, windows)])

    arg = {'ProductData':ProductData}
    return render(request, 'shop/ShowProduct.html', arg)



@login_required(login_url="/shop/login/")
def SearchProductView(request):
    query= request.GET.get('search')
    ProductData = []
    catprods = Product.objects.values('category')
    CategoryW = {item['category'] for item in catprods}
    for DifferentCategory in CategoryW:
        prodtemp = Product.objects.filter(category=DifferentCategory)
        SearchedProduct=[item for item in prodtemp if searchMatch(query, item)]
        n = len(SearchedProduct)
        windows = n // 4 + ceil((n / 4) - (n // 4))
        if len(SearchedProduct)!= 0:
            ProductData.append([SearchedProduct, range(1, windows)])

    dataToSend = {'ProductData': ProductData}
    if len(ProductData)==0:
        messages.info(request, 'Not found the Entered Product :(')
    return render(request, 'shop/SearchProduct.html', dataToSend)


@login_required(login_url="/shop/login/")
def AboutView(request):
    return render(request, 'shop/about.html')



def CartPageView(request):
    amount= request.POST.get('amount')
    print(amount)
    return render(request, 'shop/CartPage.html', {'totalRs': amount})


@login_required(login_url="/shop/login/")
def DetailView(request, myid):

    product = Product.objects.filter(id = myid)
    return render(request, 'shop/Detail.html', {'product':product[0]})


@login_required(login_url="/shop/login/")
def PlaceOrderView(request):
    
    if request.method=="POST":
        items_json= request.POST.get('itemsJson')
        nameofUser=request.POST.get('name')
        amount= request.POST.get('amount')
        email=request.POST.get('email', '')
        address=request.POST.get('address1')
        city=request.POST.get('city')
      
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone')
        # print('Amount: ', amount)

        if (amount== '' or amount== '0'):
            # print('empty')
            messages.warning(request, 'Please Add Items To Your Cart !!')
            return redirect('/shop/')
        
        if (nameofUser == '' or address == '' or phone == ''): 
            messages.error(request, 'Please Enter the details first!')
            return redirect('/shop/PlaceOrder/')

        order = Orders(items_json= items_json, 
                       name=nameofUser, 
                       email=email, 
                       address= address, 
                       city=city, 
                       zip_code=zip_code, 
                       phone=phone, 
                       amount=amount
                       )
        order.save()
        messages.info(request, 'Order Placed Successfully...')
        thank=True
        # storing for history
        update = OrderUpdate(order_id=order.order_id, name=nameofUser, amount=amount, phone=phone, address=address)
        update.save()
        id=order.order_id

        return render(request, 'shop/FinalPlaceOrder.html', {'thank':thank, 'id':id})


    return render(request, 'shop/FinalPlaceOrder.html')

# @login_required(login_url="/shop/login/")
def searchMatch(query, item):

    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False
