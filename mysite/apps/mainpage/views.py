from django.http import Http404, HttpResponse
from django.shortcuts import render
from mainpage.models import Cars
from django.views.generic import ListView


# функция
def index(request):   # (3) и смотрит здесь на index и делает request
    car = Cars.objects.get(id=1)
    car1 = Cars.objects.get(id=2)
    car2 = Cars.objects.get(id=3)
    return render(request, 'mainpage/main.html', {'car': car, 'car1': car1, 'car2': car2})


def faq(request):
    return render(request, 'mainpage/FAQ.html')


def contacts(request):
    return render(request, 'mainpage/contacts.html')


def Volkswagen_Touareg(request):
    return render(request, 'cars/Volkswagen_Touareg.html')



'''
class CarListView(ListView):
    model = Cars
    template_name = 'mainpage/main.html'
    context_object_name = 'car_list'
    queryset = Cars.objects.all()

'''




