from django.urls import path

from coffee.views import home_view, about_view, coffees_view, blog_view, contact_view

app_name = 'coffee'

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('coffees/', coffees_view, name='coffees'),
    path('blog/', blog_view, name='blog'),
    path('contact/', contact_view, name='contact')
]