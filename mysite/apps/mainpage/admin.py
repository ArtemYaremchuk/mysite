from django.contrib import admin

from .models import Cars
from .models import RentalCar


admin.site.register(Cars)
admin.site.register(RentalCar)
