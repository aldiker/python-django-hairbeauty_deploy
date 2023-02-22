from django.db import models
from django.urls import reverse


class NavBar(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    url = models.CharField(max_length=100, blank=True, verbose_name="Адрес")
    name = models.CharField(max_length=50, verbose_name="Имя")
    page = models.CharField(max_length=50, blank=True, verbose_name="Страница")
    order = models.IntegerField(verbose_name="Порядок")
    enable = models.BooleanField(default=True, verbose_name="Включен")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Навигация"
        verbose_name_plural = "Навигация"
        ordering = ['order']


class Carousel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text_1 = models.CharField(max_length=50, verbose_name="Текст 1")
    text_2 = models.CharField(max_length=50, verbose_name="Текст 2")
    photo = models.ImageField(upload_to='carousel_img/%Y/%m/%d/', verbose_name="Фото")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Карусель в шапке"
        verbose_name_plural = "Карусели в шапке"
        ordering = ['-created_at']


class Footer(models.Model):
    contact_me_enable = models.BooleanField()
    contact_me = models.CharField(max_length=50, default='Связаться')

    follow_us_enable = models.BooleanField()
    follow_us = models.CharField(max_length=50, default='Подписаться')
    twitter_url = models.CharField(max_length=100, blank=True, verbose_name="Twitter")
    facebook_url = models.CharField(max_length=100, blank=True, verbose_name="Facebook")
    linkedin_url = models.CharField(max_length=100, blank=True, verbose_name="Linkedin")
    instagram_url = models.CharField(max_length=100, blank=True, verbose_name="Instagram")

    open_hours_enable = models.BooleanField()
    open_hours = models.CharField(max_length=50, default='Посетить')
    days_period1 = models.CharField(max_length=50, blank=True, default='Понедельник - Пятница')
    days_period2 = models.CharField(max_length=50, blank=True, default='Суббота')
    days_period3 = models.CharField(max_length=50, blank=True, default='Воскресенье')
    hours_period1 = models.CharField(max_length=20, blank=True, default='10:00 - 18:00')
    hours_period2 = models.CharField(max_length=20, blank=True, default='10:00 - 14:00')
    hours_period3 = models.CharField(max_length=20, blank=True, default='Выходной')

    newsletters_enable = models.BooleanField()
    newsletters = models.CharField(max_length=50, default='Быть в теме')


class Newsletters(models.Model):
    email = models.EmailField()
    enabled = models.BooleanField(default=True, verbose_name='Включен в рассылку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
        ordering = ['created_at']


class About(models.Model):
    header = models.CharField(max_length=50, default='Serving Since 1950')
    headerImg = models.ImageField(upload_to='about_img/%Y/%m/%d/', verbose_name="Разделительное Фото")
    contentStory = models.TextField(blank=True, verbose_name="Контент для Истории")
    contentStoryEnable = models.BooleanField(default=True, verbose_name='Показывать Историю')
    contentVision = models.TextField(blank=True, verbose_name="Контент для Видения")
    contentVisionEnable = models.BooleanField(default=True, verbose_name='Показывать Видение')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        ordering = ['pk']


class Contact(models.Model):
    phone = models.CharField(max_length=13, verbose_name="Телефон")
    address = models.CharField(max_length=100, blank=True, verbose_name="Адрес")
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Наши контакты"
        verbose_name_plural = "Наши контакты"
        ordering = ['pk']


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    serviceImg = models.ImageField(upload_to='service_img/%Y/%m/%d/', verbose_name="Фото")
    serviceText = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['pk']


class Offer(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название предложения")
    sizeOFF = models.CharField(max_length=50, verbose_name="Размер скидки")
    content = models.TextField(verbose_name="Описание")
    enable = models.BooleanField(default=False, verbose_name='Активно')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"
        ordering = ['-created_at']


class OfferBooking(models.Model):
    phone = models.CharField(max_length=13, verbose_name="Телефон", null=True)
    BookingInfo = models.CharField(max_length=200, verbose_name='Информация о бронировании')
    offer = models.ForeignKey(Offer, on_delete=models.PROTECT, verbose_name='Предложение', )

    def __str__(self):
        return self.BookingInfo

    class Meta:
        verbose_name = "Бронь по акции"
        verbose_name_plural = "Брони по акции"
        ordering = ['pk']


class MenuType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип работы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип работы"
        verbose_name_plural = "Типы работы"
        ordering = ['pk']


class Currency(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    short_name = models.CharField(max_length=3, default='', verbose_name="Коротко")
    exchange_rate = models.FloatField(default=1.0, verbose_name='Курс')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"
        ordering = ['name']


class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    price = models.FloatField(default=100.0, verbose_name='Цена')
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, verbose_name='Валюта')
    photo = models.ImageField(upload_to='menu_img/%Y/%m/%d/', verbose_name="Фото работы")
    info = models.TextField(blank=True, verbose_name="Описание")
    type = models.ForeignKey(MenuType, on_delete=models.PROTECT, verbose_name='Тип работы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"
        ordering = ['name']


class Reservation(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя клиента")
    phone = models.CharField(max_length=13, verbose_name="Телефон клиента")
    email = models.EmailField(blank=True, verbose_name="Email клиента")
    date = models.DateField(verbose_name="Дата брони")
    time = models.TimeField(verbose_name="Время брони")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    number_of_reservation = models.IntegerField(verbose_name="Номер брони", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return str(self.created_at) + '   Phone: ' + self.phone

    class Meta:
        verbose_name = "Предварительная бронь"
        verbose_name_plural = "Предварительные брони"
        ordering = ['-created_at']


class Testimonial(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя клиента")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    photo = models.ImageField(blank=True, upload_to='testimonial_img/%Y/%m/%d/', verbose_name="Фото клиента")
    profession = models.CharField(blank=True, max_length=50, verbose_name="Профессия")
    comment = models.TextField(verbose_name="Отзыв")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    is_published = models.BooleanField(default=False, verbose_name="Опубликован")

    def __str__(self):
        return 'Имя клиента: ' + str(self.name)

    def get_absolute_url(self):
        return reverse('testimonial_item', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']
