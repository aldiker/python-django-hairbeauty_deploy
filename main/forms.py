from django import forms
from main.models import Newsletters, OfferBooking, Reservation, Testimonial


class NewslettersForm(forms.ModelForm):
    class Meta:
        model = Newsletters
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control border-light',
                                             'style': 'padding: 25px;',
                                             'placeholder': 'Ваш Email',
                                             })
        }


class OfferBookingForm(forms.ModelForm):
    class Meta:
        model = OfferBooking
        fields = ['offer', 'phone', 'BookingInfo', ]

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control p-4',
                                            'style': 'height: 60px; width: 200px;',
                                            'placeholder': 'Ваш телефон',
                                            }),
            'BookingInfo': forms.TextInput(attrs={'class': 'form-control p-4',
                                                  'style': 'height: 60px; width: 500px;',
                                                  'placeholder': 'Доп. інформація',
                                                  }),
        }


class ContactForm(forms.Form):
    you_name = forms.CharField(label='',
                               widget=forms.TextInput(attrs={
                                   'class': 'control-group form-control bg-transparent p-4',
                                   'id': 'name',
                                   'placeholder': "Ваше ім'я",
                                   'required': 'required',
                                   'data-validation-required-message': 'Please enter your name'
                               }))
    # you_email = forms.EmailField(label='',
    #                              widget=forms.TextInput(attrs={
    #                                  'class': 'control-group form-control bg-transparent p-4',
    #                                  'id': 'email',
    #                                  'placeholder': 'Your Email',
    #                                  'required': 'required',
    #                                  'data-validation-required-message': 'Please enter your email'
    #                              }))
    subject = forms.CharField(label='',
                              widget=forms.TextInput(attrs={
                                  'class': 'control-group form-control bg-transparent p-4',
                                  'id': 'subject',
                                  'placeholder': 'Тема',
                                  'required': 'required',
                                  'data-validation-required-message': 'Please enter a subject'
                              }))
    message = forms.CharField(label='',
                              widget=forms.Textarea(attrs={
                                  'class': 'control-group form-control bg-transparent py-3 px-4',
                                  'rows': '5',
                                  'id': 'message',
                                  'placeholder': 'Повідомлення',
                                  'required': 'required',
                                  'data-validation-required-message': 'Please enter your message'
                              }))


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'email', 'date', 'time', 'comment', 'number_of_reservation', ]
        labels = {
            'name': '',
            'phone': '',
            'email': '',
            'date': '',
            'time': '',
            'comment': '',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-group form-control bg-transparent border-primary p-4',
                       'placeholder': "Ім'я",
                       'style': 'color:  #eceff1;',
                       }
                ),
            'phone': forms.TextInput(
                attrs={'class': 'form-group form-control bg-transparent border-primary p-4',
                       'placeholder': 'Телефон',
                       'style': 'color:  #eceff1;',
                       }
                ),
            'email': forms.TextInput(
                attrs={'class': 'form-group form-control bg-transparent border-primary p-4',
                       'placeholder': 'Email',
                       'style': 'color:  #eceff1;',
                       }
                ),
            'date': forms.DateInput(
                attrs={'class': 'form-group form-control bg-transparent border-primary p-4 datetimepicker',
                       'placeholder': 'Дата у вигляді: DD.MM.YYYY',
                       'style': 'color:  #eceff1;',
                       },
                format='%d.%m.%Y'
                ),
            'time': forms.TimeInput(
                attrs={'class': 'form-group form-control bg-transparent border-primary p-4 datetimepicker-input',
                       'placeholder': 'Час у вигляді: 15:00',
                       'style': 'color:  #eceff1;',
                       }
                ),
            'comment': forms.Textarea(
                attrs={'class': 'form-group form-control bg-transparent border-primary p-4',
                       'placeholder': 'Ваш коментар',
                       'style': 'color:  #eceff1;',
                       'rows': '3',
                       }
                ),
            'number_of_reservation': forms.HiddenInput(),

        }


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = ['name', 'photo', 'profession', 'comment', ] #'slug', ]
        labels = {
            'name': '',
            'photo': 'Ваше фото',
            'profession': '',
            'comment': '',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-group form-control bg-transparent border-primary p-4',
                       'placeholder': "Ваше ім'я",
                       }
                ),
            'profession': forms.TextInput(
                attrs={'class': 'form-group form-control bg-transparent border-primary p-4',
                       'placeholder': 'Ваша професія',
                       }
                ),
            'comment': forms.Textarea(
                attrs={'class': 'form-group form-control bg-transparent border-primary p-4',
                       'placeholder': 'Ваш відгук',
                       'rows': '5',
                       }
                ),
        }
