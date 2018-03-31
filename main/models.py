from django.db import models


class CountryCode(models.Model):
    code = models.CharField("Country Code", max_length=2)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "CC"
        verbose_name_plural = "CCs"


class City(models.Model):
    country_code = models.ForeignKey(CountryCode, on_delete=models.CASCADE)
    ascii_city_name = models.CharField("Ascii name", max_length=128)
    city_name = models.CharField("Name", max_length=128)
    region = models.CharField("Region", max_length=2)
    population = models.IntegerField("pop")
    latitude = models.FloatField("latitude")
    longitude = models.FloatField("longitude")

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
