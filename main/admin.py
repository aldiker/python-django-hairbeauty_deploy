from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from main.models import *


class NavBarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'name', 'url', 'page', 'enable',)
    list_display_links = ('id', 'title',)
    list_editable = ('order', 'enable', 'url', 'page', )


class CarouselAdmin(admin.ModelAdmin):
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="300">')
        else:
            return 'NO PHOTO'

    get_photo.short_description = 'Фото'

    list_display = ('id', 'title', 'text_1', 'text_2', 'created_at', 'get_photo')
    list_display_links = ('id', 'title')
    readonly_fields = ('created_at',)


class FooterAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'contact_me_enable',
                    'follow_us_enable',
                    'open_hours_enable',
                    'newsletters_enable',
                    )
    list_display_links = ('id',)
    list_editable = ('contact_me_enable',
                     'follow_us_enable',
                     'open_hours_enable',
                     'newsletters_enable',
                     )


class NewslettersAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'enabled', 'created_at',)
    list_display_links = ('id', 'email',)
    list_editable = ('enabled',)


class AboutAdminForm(forms.ModelForm):
    contentStory = forms.CharField(widget=CKEditorUploadingWidget())
    contentVision = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = About
        fields = '__all__'


class AboutAdmin(admin.ModelAdmin):
    def get_photo(self, obj):
        if obj.headerImg:
            return mark_safe(f'<img src="{obj.headerImg.url}" width="250">')
        else:
            return 'NO PHOTO'

    get_photo.short_description = 'Разделительное фото'

    form = AboutAdminForm
    list_display = ('id',
                    'header',
                    'get_photo',
                    'contentStory',
                    'contentStoryEnable',
                    'contentVision',
                    'contentVisionEnable',
                    )
    list_display_links = ('id', 'header',)
    list_editable = ('contentStoryEnable', 'contentVisionEnable',)
    save_on_top = True


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email', 'address',)
    list_display_links = ('id',)
    list_editable = ('phone', 'email', 'address',)


class ServiceAdminForm(forms.ModelForm):
    serviceText = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Service
        fields = '__all__'


class ServiceAdmin(admin.ModelAdmin):
    def get_photo(self, obj):
        if obj.serviceImg:
            return mark_safe(f'<img src="{obj.serviceImg.url}" width="75">')
        else:
            return 'NO PHOTO'

    get_photo.short_description = 'Фото'

    form = ServiceAdminForm
    list_display = ('id',
                    'title',
                    'slug',
                    'get_photo',
                    'serviceText',
                    )
    list_display_links = ('id', 'title',)
    list_editable = ()
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True


class OfferAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'sizeOFF',
                    'content',
                    'enable',
                    'created_at',
                    )
    list_display_links = ('id', 'created_at', )
    list_editable = ('title', 'sizeOFF', 'content', 'enable',)


class OfferBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'BookingInfo', 'offer')
    list_display_links = ('id', 'phone', )
    search_fields = ('phone', 'BookingInfo',)
    list_filter = ('phone', 'offer', )


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'short_name',
                    'exchange_rate',
                    )
    list_display_links = ('id', 'name', )
    list_editable = ('short_name', 'exchange_rate',)


class MenuTypeAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    )
    list_display_links = ('id',)
    list_editable = ('name',)


class MenuAdmin(admin.ModelAdmin):
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'NO PHOTO'

    get_photo.short_description = 'Фото'

    list_display = ('id',
                    'name',
                    'slug',
                    'type',
                    'price',
                    'currency',
                    'get_photo',
                    'info',
                    )
    list_display_links = ('id', 'name', )
    list_editable = ('price', 'currency', 'type')
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'phone',
        'email',
        'date',
        'time',
        'comment',
        'number_of_reservation',
        'created_at',
    )
    list_display_links = (
        'id',
        'name',
        'phone',
        'email',
        'date',
        'time',
        'comment',
        'created_at',
    )
    readonly_fields = (
        'id',
        'name',
        'phone',
        'email',
        'date',
        'time',
        'comment',
        'created_at',
    )
    list_editable = ('number_of_reservation',)
    save_on_top = True


class TestimonialAdmin(admin.ModelAdmin):
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return 'NO PHOTO'

    get_photo.short_description = 'Фото'

    list_display = (
        'id',
        'get_photo',
        'name',
        'profession',
        'slug',
        'comment',
        'created_at',
        'is_published',
    )
    list_display_links = (
        'id',
        'name',
        'profession',
    )
    readonly_fields = (
        'created_at',
    )
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("name", "profession", )}
    save_on_top = True


admin.site.register(Carousel, CarouselAdmin)
admin.site.register(NavBar, NavBarAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(Newsletters, NewslettersAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(OfferBooking, OfferBookingAdmin)

admin.site.register(Currency, CurrencyAdmin)
admin.site.register(MenuType, MenuTypeAdmin)
admin.site.register(Menu, MenuAdmin)

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
