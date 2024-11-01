from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Flower(models.Model):
    name = models.CharField(_("Название"), max_length=255, unique=True)
    description = models.TextField(_("Описание"))
    price = models.DecimalField(_("Цена"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Цветок")
        verbose_name_plural = _("Цветы")

    def __str__(self) -> str:
        return self.name


class Bouquet(models.Model):
    name = models.CharField(_("Название"), max_length=255, unique=True)
    description = models.TextField(_("Описание"))
    price = models.DecimalField(_("Цена"), max_digits=10, decimal_places=2)
    flowers = models.ManyToManyField(Flower, through="BouquetFlower", verbose_name=_("Цветы"))

    class Meta:
        verbose_name = _("Букет")
        verbose_name_plural = _("Букеты")

    def __str__(self) -> str:
        return self.name


class BouquetFlower(models.Model):
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, verbose_name=_("Букет"))
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name=_("Цветок"))
    quantity = models.IntegerField(_(" "))

    class Meta:
        verbose_name = _("Связь цветок-букет")
        verbose_name_plural = _("Связь цветы-букет")

    def __str__(self) -> str:
        return f"{self.bouquet.name} - {self.flower.name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    order_date = models.DateField(_("Дата заказа"))
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, verbose_name=_("Букет"))
    total_price = models.DecimalField(_("Итоговая стоимость"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")

    def __str__(self) -> str:
        return f"Order {self.id} - {self.user.username}"
