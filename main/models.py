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
        return self.installments


class Apartment(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.ManyToManyField(ImageApartment)
    count_apartment = models.IntegerField(default=0)
    floors = models.IntegerField(default=0)
    height = models.IntegerField(default=3, verbose_name="Uyning balandligi")
    # type_apartment = models.ForeignKey(TypeApartment, on_delete=models.CASCADE)
    # installments = models.ForeignKey(Installments, on_delete=models.CASCADE)
    parking = models.CharField(max_length=255)
    repair = models.CharField(max_length=255)
    class_housing = models.CharField(max_length=25)
    balcony = models.BooleanField(default=False)
    attenuation_system = models.CharField(max_length=255, verbose_name="Isitish tizimi")
    territory = models.CharField(max_length=255, verbose_name="Hudud")

    def __str__(self):
        return self.name



