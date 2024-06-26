from django.shortcuts import render, redirect

from coffee.forms import ContactModelForm
from coffee.models import CoffeeModel, CoffeeAbout, BlogModel, AboutModel, ContactModel


def home_view(request):
    coffees = CoffeeModel.objects.all()
    about_coffees = CoffeeAbout.objects.all()
    blogs = BlogModel.objects.all()
    abouts = AboutModel.objects.all()
    context = {
        "coffees": coffees,
        "about_coffees": about_coffees,
        "blogs": blogs,
        "abouts": abouts,
    }
    return render(request, 'index.html', context=context)


def contact_page_view(request):
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("coffee:home")
    else:
        return render(request, template_name="index.html")


def about_view(request):
    abouts = AboutModel.objects.all()
    context = {
        "abouts": abouts
    }
    return render(request, 'about.html', context=context)


def coffees_view(request):
    about_coffees = CoffeeAbout.objects.all()
    context = {
        "about_coffees": about_coffees
    }
    return render(request, 'coffees.html', context=context)


def blog_view(request):
    blogs = BlogModel.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, 'blog.html', context=context)


def contact_view(request):
    contacts = ContactModel.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, 'contact.html', context=context)