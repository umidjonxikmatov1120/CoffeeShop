from django.db import models


class CoffeeModel(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'coffee'
        verbose_name_plural = 'coffees'


class CoffeeAbout(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'aboutcoffee'
        verbose_name_plural = 'aboutcoffees'


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'


class AboutModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'