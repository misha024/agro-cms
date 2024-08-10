from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.db import models


class MainSettings(models.Model):
    site_name = models.CharField('Название сайта', max_length=250)
    site_description = models.CharField('Описание сайта', max_length=250)
    site_domain = models.CharField('Доменное имя сайта', max_length=250, default='localhost')
    index_color = ColorField(default='#91A323')
    telegram_token = models.CharField('Телеграм токен', max_length=250, blank=True, null=True)
    telegram_group = models.CharField('Телеграм айди группы', max_length=250, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk and MainSettings.objects.exists():
            raise ValidationError('Может существовать только одна запись MainSettings')
        return super(MainSettings, self).save(*args, **kwargs)

    def __str__(self):
        return "Настройки сайта"

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"


class Contacts(models.Model):
    phone = models.CharField('Телефон', max_length=250)
    email = models.CharField('Почта', max_length=250)
    telegram = models.CharField('Телеграм', max_length=250)

    def __str__(self):
        return f"Контакты"

    def save(self, *args, **kwargs):
        if not self.pk and Contacts.objects.exists():
            raise ValidationError('Может существовать только одна запись Contacts')
        return super(Contacts, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class ProductsCategory(models.Model):
    name = models.CharField('Название', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория продуктов"
        verbose_name_plural = "Категории продуктов"


class Products(models.Model):
    category = models.ForeignKey(ProductsCategory, verbose_name='Категория',
                                 on_delete=models.CASCADE, related_name='product')
    name = models.CharField('Название', max_length=250)
    logo = models.ImageField('Логотип', upload_to='products_logo', help_text='130x130', null=True, blank=True)

    def __str__(self):
        return f"[{self.category.name}] {self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class SliderCardsDescriptions(models.Model):
    description = models.CharField('Описание', max_length=250)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"


class SliderCards(models.Model):
    title = models.CharField('Название', max_length=250)
    descriptions = models.ManyToManyField(SliderCardsDescriptions, verbose_name='Преимущества', blank=True)
    logo = models.ImageField('Логотип', upload_to='slider_cards_image', null=True, blank=True)
    href = models.URLField("Ссылка", max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Карточка слайдера"
        verbose_name_plural = "Карточки слайдера"
