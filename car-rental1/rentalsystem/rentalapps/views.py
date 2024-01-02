from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from .models import customusers
from .models import Car,customusers
from .models import Booking
# Create your views here.

def user_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password = request.POST['password']
        location = request.POST['location']
        company_name = request.POST['company_name']
        user = customusers.objects.create_user(username=username,first_name=first_name,last_name=last_name,user_type=0,email=email,address=address,company_name=company_name,
                                              phone=phone,password=password,location=location)
        user.save()
        # return redirect()
        return HttpResponse('create')
    else:
        return render(request, 'register.html')


def company_register(request):
    if request.method == 'POST':
        company_name = request.POST['companyname']
        username = request.POST['username']
        company_address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        location = request.POST['location']
        password = request.POST['password']
        data = customusers.objects.create_user(company_name=company_name,address=company_address,location=location,user_type=1,phone=phone,username=username,
                                               email=email,password=password)
        data.save()
        return HttpResponse("company register successful")
    else:

        return render(request,'branch.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        admin_user = authenticate(request, username=username, password=password)
        if admin_user is not None and admin_user.is_staff:
            login(request,admin_user)
            return redirect('admin:index')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 1:# company has logined
                return redirect(user_page)
            elif user.user_type == 0:# coutsomuser has has logined
                return redirect(indexs)
        else:
            return render(request, 'login.html',)

    return render(request, 'login.html')  # Render the login page for GET requests


def add_car(request):
    user = customusers.objects.get(id=request.user.id)
    if request.method == 'POST':
        name = request.POST['name']
        car_model = request.POST['car_model']
        price = request.POST['price']
        image = request.FILES['image']
        details = request.POST['details']
        new_car = Car.objects.create(company_id=user,name=name, car_model=car_model, price=price, details=details,image=image)
        new_car.save()
        return HttpResponse('Car added successfully')
    else:
        return render(request, 'addcar.html',)

def view_car(request):
    user = customusers.objects.get(id=request.user.id)
    print(user)
    data = Car.objects.filter(company_id=user.id)
    print(data)
    return render(request, 'carview.html', {'data': data})

def update_company(request):
    user = customusers.objects.get(id=request.user.id)
    if request.method == 'POST':
        company_name = request.POST['company_name']
        address = request.POST['company_address']
        location = request.POST['location']
        data = customusers.objects.update(company_name=company_name,
            address=address,
            location=location
        )
        return HttpResponse('Update successful')
    else:

        return render(request, 'update.html')

def view_user(request):
    user = customusers.objects.get(id=request.user.id)
    print(user)
    data = Car.objects.filter(company_id=user.id)
    print(data)
    return render(request, 'viewuser.html', {'data': data})





def view_car(request):
    user = customusers.objects.get(id=request.user.id)
    print(user)
    data = Car.objects.filter(company_id=user.id)
    print(data)
    return render(request, 'carview.html', {'data': data})


#
def booking(requset):
    if requset.method == 'POST':
        user = requset.POST['user']
        no_of_days = requset.POST['no_of_days']
        day = requset.POST['day']
        Total_cost = requset.POST['Total_cost']
        booking_date = requset.POST[' booking_date']
        status = requset.POST['status']
        Bookings = Booking.objects.create(user=user,no_of_days=no_of_days,day=day,Total_cost=Total_cost,booking_date=booking_date,status='pending',)


def car_request(request):
    data = customusers.objects.filter(user=request.user.id)
    return render(request, 'company_history.html',{'data':data})


def company_review(request):
    data = customusers.objects.filter()
    return render(request, 'company_history.html',{'data':data})



# def profile(request):
#     data = customusers.objects.
#     return render(request, 'profile.html', {'data': data})
#







def user_history(request):
    data = customusers.objects.all()
    return render(request, 'user_history.html',{'datta':data})

def indexs(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect(view_user)
def abouts(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'service.html')
def user_page(request):
    return render(request, 'user.html')
def cars(request):
    return render(request, 'car.html')


def details(request):
    return render(request, 'detail.html')

def bookings(request):
    return render(request, 'booking.html')