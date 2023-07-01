from django.shortcuts import render,redirect
from . models import Product,Order,OrderItem

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages
from . models import fristemail
from . models import contact_data
from . models import leave_cont


# Create your views here.


def index(request):
    context={
        'prod' : Product.objects.all()
    }
    if request.method=='POST':

        Email=request.POST.get("emailfirst")

        order_4=fristemail(
            Email=Email
           
            
        )
        order_4.save()


    return render(request,"web/index.html",context)


def about(request):
    return render(request,"web/navbar/about.html")

def service(request):
    return render(request,"web/navbar/service.html")

def product(request):
    return render(request,"web/navbar/product.html")

def contact(request):
        if request.method=='POST':
            if request.POST.get("form_type")=='form2':
                email=request.POST.get("email")

                form_1 = fristemail(

                    Email = email)

                form_1.save()
                
            elif request.POST.get("form_type")=='form1':

                name=request.POST.get("name_5")
                email=request.POST.get("email_5")
                subject=request.POST.get("subject_5")
                message=request.POST.get("message_5")

                from_2 = contact_data(

                    Name = name,
                    Email = email,
                    Subject = subject,
                    Message = message

                )
                from_2.save()


        return render(request,"web/navbar/contact.html")


def blog(request):
    return render(request,"web/navbar/blog.html")

def detail(request):

    if request.method=='POST':
            if request.POST.get("form_last")=='form6':
                email=request.POST.get("leavemail")

                form_1 = fristemail(

                    Email = email)

                form_1.save()    
                
            elif request.POST.get("form_last")=='form5':

                name=request.POST.get("name_8")
                email=request.POST.get("email_8")
                webiste=request.POST.get("webiste_8")
                comment=request.POST.get("comment_8")

                from_5 = leave_cont(

                    Name = name,
                    Email = email,
                    Webiste = webiste,
                    Comment = comment

                )
                from_5.save()


    return render(request,"web/navbar/detail.html")

def price(request):
    return render(request,"web/navbar/price.html")

def team(request):
    return render(request,"web/navbar/team.html")

def testimonial(request):
    return render(request,"web/navbar/testimonial.html")



def login1(request):
    if request.method=="POST":
        
        username=request.POST.get("name-3")
        password=request.POST.get("password-3")

        user = authenticate(username=username,password=password)
        if user is not None:
        
            login(request,user)
            return redirect('index')
        

        else:
            messages.info(request,'invalid details')
            return redirect('login')
        
       
        
    return render(request,"web/sign/login.html")



def sign(request):

    if request.method=="POST":
        username=request.POST.get("username-3")
        First_name=request.POST.get("firstname-3")
        Last_name=request.POST.get("lastname-3")
        email=request.POST.get("email-3")
        password=request.POST.get("password-4")
        confirmpassword=request.POST.get("password-5")
    


        if password==confirmpassword:
            customer=User.objects.create_user(username,email,password)
            customer.first_name=First_name
            customer.last_name=Last_name

            customer.save()


            return redirect("login")

    return render(request,"web/sign/sign.html")

def logout(request):
    return render(request,"web/sign/login.html")






@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'web/cart/cartbuy.html')



def checkout(request):
    
    return render(request,"web/bill/checkout.html")


def phonefrom(request):
    
    if request.method=="POST":
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)

        
        cart=request.session.get('cart')
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        company=request.POST.get("company")
        country=request.POST.get("country")
        address=request.POST.get("add1")
        city=request.POST.get("town1")
        state=request.POST.get("state2")
        pincode=request.POST.get("pin1")
        phone=request.POST.get("phone1")
        email=request.POST.get("email1")
        account=request.POST.get("account1")
        

        order=Order(
            user=user,
            first_name=first_name,
            last_name=last_name,
            company=company,
            country=country,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            phone=phone,
            email=email,
            account=account,
           
            
        )
       
        order.save()
    
        for i in cart:
            a=float(cart[i]['price'])
            b=float(cart[i]['quantity'])
            total=a*b

            order1=OrderItem(
                order=order,
                Product=cart[i]['name'],
                image=cart[i]['image'],
                price=cart[i]['price'],
                qunatity=cart[i]['quantity'],
                total=total
            )

            order1.save()

    return render(request,"web/order/phonefrom.html")

def right(request):


    return render(request,"web/right/right.html")










