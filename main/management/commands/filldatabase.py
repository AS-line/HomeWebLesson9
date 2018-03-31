# coding: utf-8
from django.core.management.base import BaseCommand
from main.models import City, CountryCode
from django.db import transaction


class Command(BaseCommand):
    help = "Заносим данные в дазу банных"

    @transaction.atomic()
    def handle(self, *args, **options):
        file_path = '/home/aslan/Documents/parcing/worldcitiespop.txt'

        with open(file_path, 'r') as file:
            for line in file:
                line = line.split(",")
                city = City(ascii_city_name=line[1], city_name=line[2], region=line[3],
                            population=int(line[4]) if line[4] != '' else 0,
                            latitude=float(line[5]), longitude=float(line[6]))
                country_code, created = CountryCode.objects.get_or_create(code=line[0])
                city.country_code = country_code
                print(city.ascii_city_name)
                city.save()
                self.stdout = 'Банные занесены'
