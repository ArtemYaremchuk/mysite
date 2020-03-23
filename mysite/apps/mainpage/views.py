from django.http import Http404, HttpResponse
from django.shortcuts import render
from mainpage.models import Cars
from django.views.generic import ListView


# функция
#def index(request):   # (3) и смотрит здесь на index и делает request
 #   car = Cars.objects.get(id=1)
  #  return render(request, 'mainpage/main.html', {'car': car})

def index(request):
    return render(request, 'mainpage/FAQ.html')


def in_category(things, category):
    return things.filter(category=category)

class CarListView(ListView):
    model = Cars
    template_name = 'mainpage/main.html'
    context_object_name = 'car_list'
    queryset = Cars.objects.all()

   # def get_queryset(self):

      #  return Cars.objects.all()






