from django.db import models


class Cars(models.Model):

    car_name = models.CharField('Название машины', max_length=90)
    car_pic = models.CharField('Картинка', max_length=100)
    doors = models.IntegerField('Количество дверей')
    petrol = models.FloatField('Бензин на 100км')
    luggage = models.IntegerField('Багаж')
    price26 = models.IntegerField('цена на 26 суток', )
    price10 = models.IntegerField('цена на 10-25 суток', )
    price4 = models.IntegerField('цена на 4-9 суток', )
    price1 = models.IntegerField('цена на 1-3 суток', )

    def __str__(self):
        return self.car_name

    class Meta:  # переименовать с англ
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class RentalCar(models.Model):
    name = models.CharField('Имя заказчика', max_length=50)
    number = models.IntegerField('Номер телефона')
    email = models.EmailField('Электронная почта')
    message = models.CharField('Сообщение', max_length=300)
    rental = models.BooleanField('Аренда с залогом',)
    rental_without = models.BooleanField('Аренда без залога',)
    wheels_glass_insurance = models.BooleanField('Страховка колес и стекла',)
    rental_navigator = models.BooleanField('Аренда навигатора',)
    child_seat_rental = models.BooleanField('Аренда детского кресла',)
    Unlimited_mileage = models.BooleanField('Неограниченый пробег',)


    def __str__(self):
        return self.name

    class Meta:  # переименовать с англ
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренда заказы'