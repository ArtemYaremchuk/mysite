from django.db import models


class RentalCar(models.Model):
    car_name = models.CharField("Название машины", max_length=50)
    data_start = models.CharField('Дата начала аренды', max_length=50)
    data_end = models.CharField('Дата окончания аренды', max_length=50)
    name = models.CharField('Имя заказчика', max_length=50)
    number = models.IntegerField('Номер телефона')
    email = models.EmailField('Электронная почта')
    message = models.CharField('Сообщение', max_length=300)
    rental = models.BooleanField('Аренда с залогом', default=False)
    rental_without = models.BooleanField('Аренда без залога', default=False)
    wheels_glass_insurance = models.BooleanField('Страховка колес и стекла', default=False)
    rental_navigator = models.BooleanField('Аренда навигатора', default=False)
    child_seat_rental = models.BooleanField('Аренда детского кресла', default=False)
    Unlimited_mileage = models.BooleanField('Неограниченый пробег', default=False)


    def __str__(self):
        return self.name

    class Meta:  # переименовать с англ
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренда заказы'