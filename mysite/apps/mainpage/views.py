from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.shortcuts import render
from mainpage.models import RentalCar


# функция
# получение данных из БД
def index(request):   # (3) и смотрит здесь на index и делает request
    return render(request, 'mainpage/main.html',)


def faq(request):
    return render(request, 'mainpage/FAQ.html')


def contacts(request):
    return render(request, 'mainpage/contacts.html')


def Volkswagen_Touareg(request):
        return render(request, 'cars/Volkswagen_Touareg.html',)


def volkswagen_golf_r_2017(request):
    return render(request, 'cars/Volkswagen_Golf_R_2017.html',)


def mitsubishi_lancer_2015(request):
    return render(request, 'cars/Mitsubishi_Lancer_2015.html',)


def mitsubishi_outlander(request):
    return render(request, 'cars/Mitsubishi_Outlander.html',)


def toyota_corolla_2016(request):
    return render(request, 'cars/Toyota_Corolla_2016.html')


def chevrolet_cruze(request):
    return render(request, 'cars/Chevrolet_Cruze.html')


def rental_take_car(request):
    if request.method == "POST":
        rental_car = RentalCar()
        rental_car.data_start = request.POST.get("dataS")
        rental_car.data_end = request.POST.get("dateE")
        rental_car.name = request.POST.get("name")
        rental_car.number = request.POST.get("number")
        rental_car.email = request.POST.get("email")
        rental_car.message = request.POST.get("message")
        rental_car.rental = request.POST.get("rental") == 'on'
        rental_car.rental_without = request.POST.get("rental_without") == 'on'
        rental_car.wheels_glass_insurance = request.POST.get("wheels_glass_insurance") == 'on'
        rental_car.rental_navigator = request.POST.get("rental_navigator") == 'on'
        rental_car.child_seat_rental = request.POST.get("child_seat_rental") == 'on'
        rental_car.Unlimited_mileage = request.POST.get("Unlimite d_mileage") == 'on'
        rental_car.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


