from django.contrib import admin
from coffee.models import CoffeeModel, CoffeeAbout, BlogModel, AboutModel

admin.site.register(CoffeeModel)
admin.site.register(CoffeeAbout)
admin.site.register(BlogModel)
admin.site.register(AboutModel)
