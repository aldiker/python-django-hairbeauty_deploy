from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Max
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, CreateView, DetailView

from main.models import *
from .forms import NewslettersForm, ContactForm, OfferBookingForm, ReservationForm, TestimonialForm
from .templatetags.main_tags import get_offer


def page404(request, exception):
    return HttpResponseNotFound('<h1>Такой страница не существует</h1>')


def menu(request):
    title = 'Menu'

    context = {
        'title': title,
    }
    return render(request, 'main/menu.html', context)


# Возвращает форму из POST запроса, по префиксу (должен совпадать с name=prefix на кнопке Submit)
# def _get_form(request, form_cls, prefix):        # возвращает форму из запроса по префиксу
#     data = request.POST if prefix in request.POST else None
#     return form_cls(data, prefix=prefix)


def _get_reservation_form(request, form_cls, prefix):

    if request.method == 'POST' and prefix in request.POST:
        print('_get_reservation_form - POST!!!')
        form = form_cls(request.POST)

        if form.is_valid():
            print('_get_reservation_form - VALID!!!')
            new_res = form.save(commit=False)
            print(form.cleaned_data)
            print(Reservation.objects.aggregate(max_number=Max('number_of_reservation')))
            max_number = Reservation.objects.aggregate(max_number=Max('number_of_reservation'))['max_number']
            if max_number:
                new_res.number_of_reservation = max_number + 1
            else:
                new_res.number_of_reservation = 1
            new_res.save()
            messages.success(request,
                             'Ваша заявка принята. Мы Вам обязательно перезвоним!',
                             extra_tags='_reservation')
        else:
            print('_get_reservation_form - NOT VALID !!!')
            print(form.errors)
            messages.error(request,
                           'Форма заполнена неверно. Исправьте пожалуйста.',
                           extra_tags='_reservation')
    else:
        form = form_cls()

    return form


def _get_offerbooking_form(request, form_cls, prefix):

    if request.method == 'POST' and prefix in request.POST:
        print('_get_offerbooking_form - POST!!!')
        form = form_cls(request.POST)

        if form.is_valid():
            print('_get_offerbooking_form - VALID!!!')
            form.save()
            messages.success(request,
                             'Ваша заявка принята. Мы Вам обязательно перезвоним!',
                             extra_tags='_offerbooking')
        else:
            print('_get_offerbooking_form - NOT VALID !!!')
            print(form.errors)
            messages.error(request,
                           'Форма заполнена неверно. Исправьте пожалуйста.',
                           extra_tags='_offerbooking')
    else:
        form = form_cls(initial={'offer': get_offer()})

    return form


def _get_newsletters_form(request, form_cls, prefix):

    if request.method == 'POST' and prefix in request.POST:
        print('_get_newsletters_form - POST!!!')
        form = form_cls(request.POST)

        if form.is_valid():
            print('_get_newsletters_form - VALID!!!')
            form.save()
            messages.success(request,
                             'Спасибо. Мы Вас запомнили!',
                             extra_tags='_newsletters')
        else:
            print('_get_newsletters_form - NOT VALID !!!')
            print(form.errors)
            messages.error(request,
                           'Это не похоже на email :-)',
                           extra_tags='_newsletters')
    else:
        form = form_cls()

    return form


def index(request):

    # todo Подумать как объединить в одну функцию.
    reservation_form = _get_reservation_form(request, ReservationForm, 'reservation_form_submit')
    newsletters_form = _get_newsletters_form(request, NewslettersForm, 'newsletters_form_submit')
    offerbooking_form = _get_offerbooking_form(request, OfferBookingForm, 'offerbooking_form_submit')

    carousel = Carousel.objects.all()
    footer = Footer.objects.all().first()
    testimonial_items = Testimonial.objects.all()

    context = {
        'carousel': carousel,
        'footer': footer,
        'newsletters_form': newsletters_form,
        'offerbooking_form': offerbooking_form,
        'reservation_form': reservation_form,
        'testimonial_items': testimonial_items,
    }
    return render(request, 'main/index.html', context)


def about(request):
    title = 'About Us'

    context = {
        'title': title,
    }
    return render(request, 'main/about.html', context)


def about_lean_more(request, story_vision):

    if story_vision == 'story':
        title = 'About Our Story'
    elif story_vision == 'vision':
        title = 'About Our Vision'
    else:
        raise Http404()

    context = {
        'title': title,
        'story_vision': story_vision,
    }
    return render(request, 'main/about_lean_more.html', context)


def service(request):
    title = 'Services'

    context = {
        'title': title,
    }
    return render(request, 'main/service.html', context)


def offer(request):

    offerbooking_form = _get_offerbooking_form(request, OfferBookingForm, 'offerbooking_form_submit')
    title = 'Акции'

    context = {
        'title': title,
        'offerbooking_form': offerbooking_form,
    }
    return render(request, 'main/offer.html', context)


def reservation(request):

    reservation_form = _get_reservation_form(request, ReservationForm, 'reservation_form_submit')
    title = 'Бронирование'

    context = {
        'title': title,
        'reservation_form': reservation_form,
    }
    return render(request, 'main/reservation.html', context)


def contact(request):
    title = 'Contact'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('Данные формы верны - form.is_valid!!!!')

            try:
                text_message = 'From: ' + form.cleaned_data['you_name'] + form.cleaned_data['message']
                result = send_mail(str(form.cleaned_data['you_name']) + ' - ' + str(form.cleaned_data['subject']),
                                   form.cleaned_data['message'],
                                   'diker_test@ukr.net',    # адрес источника
                                   ['aldiker@ukr.net', 'diker_test@ukr.net'],     # список адресатов
                                   fail_silently=False,     # сервер будет сообщать об ошибках отправки
                                   )
                if result:
                    print('Письмо успешно отправлено')
                    messages.success(request, 'Письмо успешно отправлено')
                    return redirect('contact')
                else:
                    print('Не получилось отправить письмо')
                    messages.error(request, 'Не получилось отправить письмо')

            except Exception as z:
                print('Не получилось отправить письмо: ', z)
                messages.error(request, 'Не получилось отправить письмо')

        else:
            print('Данные формы не верны')
            messages.error(request, 'Данные формы не верны')
    else:
        form = ContactForm()

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'main/contact.html', context)


class TestimonialList(ListView):
    model = Testimonial
    template_name = 'main/testimonial.html'
    context_object_name = 'testimonial_items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TestimonialList, self).get_context_data(**kwargs)
        context['title'] = 'Отзывы'
        return context

    def get_queryset(self):
        return Testimonial.objects.filter(is_published=True)


class TestimonialDetail(DetailView):
    model = Testimonial
    context_object_name = 'item'
    template_name = 'main/testimonial_item.html'
    # slug_url_kwarg = 'slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TestimonialDetail, self).get_context_data(**kwargs)
        context['title'] = 'Отзыв'
        return context


class TestimonialCreate(CreateView):
    form_class = TestimonialForm
    template_name = 'main/testimonial_create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TestimonialCreate, self).get_context_data(**kwargs)
        context['title'] = 'Добавить отзыв'
        return context
