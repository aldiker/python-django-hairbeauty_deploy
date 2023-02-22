from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('offer/', offer, name='offer'),
    path('menu/', menu, name='menu'),
    path('reservation/', reservation, name='reservation'),
    path('testimonial/', TestimonialList.as_view(), name='testimonial'),
    path('contact/', contact, name='contact'),
    path('about_lean_more/<str:story_vision>/', about_lean_more, name='about_lean_more'),

    path('main/testimonial_item/<slug:slug>', TestimonialDetail.as_view(), name='testimonial_item'),
    path('main/testimonial_create', TestimonialCreate.as_view(), name='testimonial_create'),
]
