from django.db import models


# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banner-image')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ImageApartment(models.Model):
    image = models.ImageField(upload_to='apartment-image')


class TypeApartment(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Installments(models.Model):
    installments = models.IntegerField(default=0)

    def __str__(self):
        return str(self.installments)


class Apartment(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.ManyToManyField(ImageApartment)
    count_apartment = models.IntegerField(default=0)
    floors = models.IntegerField(default=0)
    height = models.IntegerField(default=3, verbose_name="Uyning balandligi")
    type_apartment = models.ForeignKey(TypeApartment, on_delete=models.CASCADE)
    installments = models.ForeignKey(Installments, on_delete=models.CASCADE)
    parking = models.CharField(max_length=255)
    repair = models.CharField(max_length=255)
    class_housing = models.CharField(max_length=25)
    balcony = models.BooleanField(default=False)
    attenuation_system = models.CharField(max_length=255, verbose_name="Isitish tizimi")
    territory = models.CharField(max_length=255, verbose_name="Hudud")
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ImageDesign(models.Model):
    image = models.ImageField(upload_to='design-image')


class DesignApartment(models.Model):
    title = models.CharField(max_length=255)
    image = models.ManyToManyField(ImageDesign)


class TypePurchase(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=125)
    image = models.FileField(upload_to='purchase-image')


class BannerDiscount(models.Model):
    background = models.ImageField(upload_to='banner-footer-background')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    discount = models.IntegerField(default=0)


class Info(models.Model):
    background = models.ImageField(upload_to='info-background')
    title = models.CharField(max_length=255)
    description = models.TextField()


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    background = models.ImageField(upload_to='contact-us-background')
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=150)
    contact = models.ForeignKey(ContactUs, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Footer(models.Model):
    icon = models.ImageField(upload_to='footer-icon')
    telegram = models.URLField()
    instagram = models.URLField()
    youtube = models.URLField()
    facebook = models.URLField()


class GoodRealtor(models.Model):
    icon = models.ImageField(upload_to='realtor-icon')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class UsefulRealtor(models.Model):
    icon = models.ImageField(upload_to='realtor-icon')
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=150)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_photo = models.ImageField(upload_to='profile-photo')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Realtor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()


class Work(models.Model):
    icon = models.ImageField(upload_to='work-icon')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)


