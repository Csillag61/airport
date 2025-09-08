from django.test import TestCase
from .models import Country, City, Airport

class CountryModelTest(TestCase):
    def test_str(self):
        country = Country.objects.create(name="Ukraine")
        self.assertEqual(str(country), "Ukraine")

class CityModelTest(TestCase):
    def test_str(self):
        country = Country.objects.create(name="Spain")
        city = City.objects.create(name="Barcelona", country=country)
        self.assertEqual(str(city), "Barcelona, Spain")

class AirportModelTest(TestCase):
    def test_str(self):
        country = Country.objects.create(name="France")
        city = City.objects.create(name="Paris", country=country)
        airport = Airport.objects.create(name="CDG", city=city, closest_big_city="Paris")
        self.assertEqual(str(airport), "CDG")
