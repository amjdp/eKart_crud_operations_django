from django.shortcuts import render

from customer.models import Customer

# Create your views here.


def customer_home(request):
    return render(request, 'customer/customer_home.html')


def store(request):
    return render(request, 'customer/store.html')


def product_detail(request):
    return render(request, 'customer/product_detail.html')


def cart(request):
    return render(request, 'customer/cart.html')


def place_order(request):
    return render(request, 'customer/place_order.html')


def order_complete(request):
    return render(request, 'customer/order_complete.html')


def dashboard(request):
    return render(request, 'customer/dashboard.html')


def seller_register(request):
    return render(request, 'customer/seller_register.html')


def seller_login(request):
    return render(request, 'customer/seller_login.html')


def customer_signup(request):
    message = ''
    status = False
    if request.method == 'POST':  
        fname = request.POST['fname'] 
        lname = request.POST['lastname']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        password = request.POST['password']

        customer_exist = Customer.objects.filter(email = email).exists()

        if not customer_exist: 

            customer = Customer(first_name = fname, last_name = lname , gender = gender, email = email, 
                        city = city, country = country, password = password)
            customer.save()
            message = 'Registration Succesful'
            status = True
        
        else:
            message = 'Email Exists'     

    return render(request, 'customer/customer_signup.html',{'message': message, 'status': status})


def customer_login(request):
    return render(request, 'customer/customer_login.html')


def forgot_password_customer(request):
    return render(request, 'customer/forgot_password_customer.html')


def forgot_password_seller(request):
    return render(request, 'customer/forgot_password_seller.html')